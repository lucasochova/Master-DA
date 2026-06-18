# convertir_ipynb_a_py.ps1
#
# Convierte todos los archivos .ipynb de un directorio a .py
# usando jupyter nbconvert. La salida se guarda en la misma carpeta.
#
# Requisitos: tener instalado Jupyter (pip install jupyter)
#
# Uso:
#   .\convertir_ipynb_a_py.ps1 [-Carpeta <ruta>]
#
# Si no se indica parametro:
#   - Carpeta por defecto: el directorio actual (.)

param(
    [string]$Carpeta = "."
)

# Comprobar que el directorio existe
if (-not (Test-Path -Path $Carpeta -PathType Container)) {
    Write-Error "El directorio '$Carpeta' no existe."
    exit 1
}

# Comprobar que python esta disponible
$pythonDisponible = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonDisponible) {
    Write-Error "No se encontro 'python' en el PATH. Instala Python desde https://www.python.org/downloads/"
    exit 1
}

# Comprobar que nbconvert esta instalado (se usa como modulo de python,
# evita problemas de PATH con el comando 'jupyter')
python -m nbconvert --version > $null 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Error "No se encontro el modulo 'nbconvert'. Instalalo con: pip install jupyter"
    exit 1
}

$notebooks = Get-ChildItem -Path $Carpeta -Filter *.ipynb -File

if ($notebooks.Count -eq 0) {
    Write-Host "No se encontraron archivos .ipynb en '$Carpeta'."
    exit 0
}

$contador = 0

foreach ($nb in $notebooks) {
    Write-Host "Convirtiendo: $($nb.Name)"
    python -m nbconvert --to script $nb.FullName --output-dir $Carpeta

    if ($LASTEXITCODE -eq 0) {
        $contador++
    } else {
        Write-Warning "Fallo al convertir: $($nb.Name)"
    }
}

Write-Host ""
Write-Host "Listo. Se convirtieron $contador de $($notebooks.Count) archivo(s) .ipynb a .py en '$Carpeta'"
