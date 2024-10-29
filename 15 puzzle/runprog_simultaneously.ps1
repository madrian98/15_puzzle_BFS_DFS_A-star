# Define the orders for BFS and DFS strategies
$Orders = @('RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD')

# Run BFS strategy for each order
foreach ($order in $Orders) {
    try {
        Start-Process powershell.exe -ArgumentList "./runprog.ps1 bfs $order"
    } catch {
        Write-Error "Failed to start process for BFS with order ${order}: $_"
    }
}

# Run DFS strategy for each order
foreach ($order in $Orders) {
    try {
        Start-Process powershell.exe -ArgumentList "./runprog.ps1 dfs $order"
    } catch {
        Write-Error "Failed to start process for DFS with order ${order}: $_"
    }
}

# Run A* strategy with different heuristics
try {
    Start-Process powershell.exe -ArgumentList "./runprog.ps1 astr hamm"
} catch {
    Write-Error "Failed to start process for A* with heuristic hamm: $_"
}

try {
    Start-Process powershell.exe -ArgumentList "./runprog.ps1 astr manh"
} catch {
    Write-Error "Failed to start process for A* with heuristic manh: $_"
}