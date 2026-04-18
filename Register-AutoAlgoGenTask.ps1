# 관리자 권한 없이, 현재 사용자 로그온 시 매번 실행되도록 예약 작업을 등록합니다.
# 제거: Unregister-ScheduledTask -TaskName "AutoAlgoGenAtLogon" -Confirm:$false

$TaskName = "AutoAlgoGenAtLogon"
$ScriptPath = Join-Path $PSScriptRoot "run_daily_problem_gen.ps1"

if (-not (Test-Path -LiteralPath $ScriptPath)) {
    Write-Error "없음: $ScriptPath"
    exit 1
}

$arg = "-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File `"$ScriptPath`""
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument $arg
$trigger = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited

Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal | Out-Null

Write-Host "등록됨: 작업 스케줄러 > '$TaskName' (로그온 시 run_daily_problem_gen.ps1 실행)"
Write-Host "로그: $PSScriptRoot\auto_gen_history.log"
