@echo off
chcp 65001 > nul

echo ===================================================
echo       INICIANDO PROJETO: ANALISE ODORANTE
echo ===================================================

:: Navega para a pasta do arquivo
cd /d "%~dp0"

:: Se a venv não existir, cria de forma direta
if not exist .venv python -m venv .venv

echo [1/2] Ativando ambiente virtual...
call .venv\Scripts\activate.bat

echo [2/2] Atualizando dependencias...
pip install -r requirements.txt -q

echo.
echo ===================================================
echo Executando main.py...
echo ===================================================
echo.

python main.py

echo.
echo ===================================================
echo Processo finalizado.
echo ===================================================
echo Pressione qualquer tecla para fechar esta janela...
pause > nul