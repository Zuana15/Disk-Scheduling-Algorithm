# main.py
import matplotlib.pyplot as plt
from rich.console import Console
from rich.table import Table
import algorithms as algo
import visualizer as viz

console = Console()

def get_user_input():
    console.print("\n[bold cyan]--- Disk Scheduling Setup ---[/bold cyan]")
    head = int(console.input("[bold]Enter initial head position: [/bold]"))
    req_str = console.input("[bold]Enter requests (comma separated): [/bold]")
    req = [int(x.strip()) for x in req_str.split(',')]
    return head, req

def main_menu():
    console.print("\n[bold magenta]╔══════════════════════════════════════╗[/bold magenta]")
    console.print("[bold magenta]║   OS Disk Scheduling Visualizer     ║[/bold magenta]")
    console.print("[bold magenta]╚══════════════════════════════════════╝[/bold magenta]")
    
    head, req = get_user_input()
    
    while True:
        console.print("\n[bold yellow]Select an option:[/bold yellow]")
        console.print("1. Run FCFS")
        console.print("2. Run SSTF")
        console.print("3. Run SCAN")
        console.print("4. Run C-SCAN")
        console.print("5. COMPARE ALL (Generates 1 overlay graph)")
        console.print("0. Exit")
        
        choice = console.input("[bold]>> [/bold]")
        
        if choice == '5':
            results = [
                ("FCFS", *algo.fcfs(req, head)),
                ("SSTF", *algo.sstf(req, head)),
                ("SCAN", *algo.scan(req, head, 200)),
                ("C-SCAN", *algo.cscan(req, head, 200))
            ]
            

            viz.plot_comparison(results, 200)       
            viz.plot_comparison_grid(results, 200)  
            

            plt.show()             
            
            console.print("[bold green]✅ Generated 'comparison_overlay.png' and 'comparison_grid.png'[/bold green]")
            
        elif choice in ['1', '2', '3', '4']:
            funcs = {'1': ('FCFS', algo.fcfs), '2': ('SSTF', algo.sstf), 
                     '3': ('SCAN', algo.scan), '4': ('C-SCAN', algo.cscan)}
            name, func = funcs[choice]
            path, seek = func(req, head, 200) if choice in ['3','4'] else func(req, head)
            
            #table
            table = Table(title=f"{name} Results")
            table.add_column("Metric", style="cyan")
            table.add_column("Value", style="green")
            table.add_row("Total Seek Time", str(seek))
            table.add_row("Path Taken", " -> ".join(map(str, path)))
            console.print(table)
            
            file = viz.plot_single(name, path, seek, 200)
            console.print(f"[bold green]✅ Generated '{file}'[/bold green]")
            
        elif choice == '0':
            break

if __name__ == "__main__":
    main_menu()