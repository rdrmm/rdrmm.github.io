# call-home.ps1

$responseObj = $response | ConvertFrom-Json

switch ($responseObj.action) {
    "none"   { return }
    "sleep"  { Start-Sleep -Seconds $responseObj.seconds }
    "run"    {
        $out = powershell -NoProfile -Command $responseObj.command 2>&1
        # Optionally: send result back in a second SSH call or next heartbeat
    }
    "download" {
        Invoke-WebRequest -Uri $responseObj.url -OutFile $responseObj.path
    }
    "upload" {
        # e.g., scp or curl to your server
    }
}

$server = "agent@portal.solutionsdx.com"
$identity = "C:\ProgramData\myagent\id_rsa"   # per-client key

$json = & "$PSScriptRoot\collect-info.ps1"

# Use stdin to send JSON, expect JSON back
$cmd = "agent/heartbeat"
$sshArgs = @(
    "-i", $identity,
    "-o", "BatchMode=yes",
    "-o", "ConnectTimeout=5",
    "-o", "ServerAliveInterval=10",
    "-o", "ServerAliveCountMax=1",
    $server, $cmd
)

# simple retry with backoff
$maxAttempts = 3
for ($attempt = 1; $attempt -le $maxAttempts; $attempt++) {
    try {
        $response = $json | ssh @sshArgs 2>$null
        if ($LASTEXITCODE -eq 0 -and $response) {
            $response
            break
        }
    } catch {}
    Start-Sleep -Seconds (5 * $attempt)
}
