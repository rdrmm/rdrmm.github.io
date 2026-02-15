# collect-info.ps1
$os   = Get-CimInstance Win32_OperatingSystem
$cs   = Get-CimInstance Win32_ComputerSystem
$disk = Get-CimInstance Win32_LogicalDisk -Filter "DriveType=3" | 
        Select-Object -First 1
$cpu  = Get-CimInstance Win32_Processor | Select-Object -First 1
$mem  = Get-CimInstance Win32_OperatingSystem

# persistent client ID (stored once)
$idFile = "$env:ProgramData\myagent-id.txt"
if (-not (Test-Path $idFile)) {
    [guid]::NewGuid().ToString() | Out-File -FilePath $idFile -Encoding ASCII -NoNewline
}
$clientId = Get-Content $idFile -Raw

$uptimeSec = [int](New-TimeSpan -Start $os.LastBootUpTime -End (Get-Date)).TotalSeconds

$obj = [pscustomobject]@{
    id            = $clientId
    hostname      = $env:COMPUTERNAME
    os            = "$($os.Caption) $($os.Version)"
    uptime        = $uptimeSec
    agent_version = "1.0"
    capabilities  = @{
        run      = $true
        upload   = $true
        download = $true
    }
    metrics       = @{
        cpu          = [int]$cpu.LoadPercentage
        mem_free_mb  = [int]($mem.FreePhysicalMemory / 1024)
        disk_free_gb = [int]($disk.FreeSpace / 1GB)
    }
}

$obj | ConvertTo-Json -Compress
