# 매일 지정 시각에 한 번 실행 (PC가 켜져 있을 때). 시각은 아래 $At 수정.
# 등록: powershell -ExecutionPolicy Bypass -File .\Register-AutoAlgoGenTaskDaily.ps1

$TaskName = "AutoAlgoGenDaily"
$ScriptPath = Join-Path $PSScriptRoot "run_daily_problem_gen.ps1"
$At = "09:00"   # 24시간제 로컬 시각

if (-not (Test-Path -LiteralPath $ScriptPath)) {
    Write-Error "없음: $ScriptPath"
    exit 1
}

$arg = "-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File `"$ScriptPath`""
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument $arg
$trigger = New-ScheduledTaskTrigger -Daily -At $At
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited

Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal | Out-Null

Write-Host "등록됨: 매일 $At 에 '$TaskName' 실행"
