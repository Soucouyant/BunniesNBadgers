@echo off
ping -n 2 127.0.0.1 > nul 

for %%i in (*.png) do identify %%i
for %%i in (*.png) do convert %%i -strip %%i 
for %%i in (*.png) do identify %%i 

echo done

ping -n 2 127.0.0.1 > nul