Function GetIP {
   $IP = Get-NetIPAddress | Where-Object {$_.IPv4Address -like '192*'}
   return $IP.IPv4Address
}