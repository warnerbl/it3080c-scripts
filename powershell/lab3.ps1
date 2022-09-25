

function getIP { (Get-NetIPAddress).IPv4Address	| Select-String ("192*") }
function getUser { $env:USERNAME.ToLower() } 
function getHost { hostname }
function getPowerShellVersion { $Host.Version.Major }
function getDate { Get-Date -Format "dddd MM/dd/yyyy" }

$IP = getIP
$USER = getUser
$HOSTNAME = getHost
$POWERSHELL = getPowerShellVersion
$DATE = getDate


Write-Host("This machine's IP is $IP. User is $USER. Hostname is $HOSTNAME. PowerShell Version $POWERSHELL. Today's date is $DATE")
