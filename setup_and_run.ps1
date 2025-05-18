
if (-Not (Test-Path -Path ".venv")) {
    python -m venv .venv
}

& .\.venv\Scripts\Activate.ps1


if (Test-Path -Path "requirements.txt") {
    python -m pip install --upgrade pip
    pip install -r requirements.txt
}

Write-Host "run ip_server.py ..."
Start-Process -NoNewWindow -FilePath python -ArgumentList "ip_server.py"


Start-Sleep -Seconds 2

Write-Host "run server.py ..."
python server.py


deactivate
