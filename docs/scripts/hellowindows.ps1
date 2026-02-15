$asset_id = (Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Cryptography").MachineGuid
$hostname = $env:COMPUTERNAME

$cs = Get-CimInstance Win32_ComputerSystem
$bios = Get-CimInstance Win32_BIOS
$cpu = Get-CimInstance Win32_Processor
$disk = Get-CimInstance Win32_DiskDrive
$os = Get-CimInstance Win32_OperatingSystem
$net = Get-CimInstance Win32_NetworkAdapterConfiguration | Where-Object { $_.MACAddress -and $_.IPAddress }

$payload = [pscustomobject]@{
    asset_id          = $asset_id
    hostname          = $hostname
    serial_number     = $bios.SerialNumber
    manufacturer      = $cs.Manufacturer
    model             = $cs.Model
    cpu               = $cpu.Name
    ram_gb            = [math]::Round($cs.TotalPhysicalMemory / 1GB)
    storage_gb        = ($disk.Size | Measure-Object -Sum).Sum / 1GB -as [int]
    mac_address       = $net.MACAddress
    ip_address        = $net.IPAddress[0]
    os_name           = $os.Caption
    os_version        = $os.Version
}

$payload | ConvertTo-Json -Depth 5

$payload | ConvertTo-Json -Depth 5 | Out-File -FilePath "c:\rdrmm-testpayload.json" -Encoding UTF8