# Wrapper to download and run the remote script with robust logging for scheduled tasks
$LogFile = 'C:\Windows\Temp\rdrmm-hellowindows.log'
function Log($msg){
  $line = "$(Get-Date -Format o) [PID:$($PID)] [User:$($env:USERNAME)] - $msg"
  $line | Out-File -FilePath $LogFile -Append -Encoding UTF8
}

Log 'Wrapper start'
Log "PowerShell version: $($PSVersionTable.PSVersion)"

# Force TLS1.2 for systems that default to older protocols
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$uri = 'https://rdrmm.github.io/scripts/hellowindows.ps1'
try{
  Log "Downloading script from $uri"
  $script = Invoke-RestMethod -Uri $uri -UseBasicParsing -TimeoutSec 30 -ErrorAction Stop
  Log "Downloaded script (length: $($script.Length))"

  Log 'Executing downloaded script'
  $output = & { Invoke-Expression $script } 2>&1
  if($output){
    Log "Script output: $([string]::Join(' | ', ($output | ForEach-Object { $_.ToString() } )))"
  } else { Log 'Script executed with no output' }
}
catch{
  Log "ERROR: $($_.Exception.Message)"
  Log "DETAILS: $($_ | Out-String)"
}

Log 'Wrapper end'
