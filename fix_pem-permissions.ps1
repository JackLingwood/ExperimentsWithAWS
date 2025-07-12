param (
    [Parameter(Mandatory = $true)]
    [string]$PemPath
)

$PemPath = Resolve-Path -Path $PemPath

if (-Not (Test-Path $PemPath)) {
    Write-Error "File not found: $PemPath"
    exit 1
}

Write-Host "Fixing permissions for: $PemPath"

# Remove inherited and broad group access
icacls $PemPath /inheritance:r | Out-Null
icacls $PemPath /remove "Users" | Out-Null
icacls $PemPath /remove "BUILTIN\Users" | Out-Null
icacls $PemPath /remove "Everyone" | Out-Null

# Grant read-only to current user
$User = whoami
icacls $PemPath /grant "$($User):(R)" | Out-Null

Write-Host "✅ Permissions updated successfully for $User"
