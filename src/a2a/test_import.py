import traceback
import sys

# Add verbosity
try:
    # Read and compile the file to check for issues
    with open('agent/product_management_agent.py', 'r') as f:
        content = f.read()
    
    print("Compiling file...")
    code = compile(content, 'product_management_agent.py', 'exec')
    print("Compilation successful!")
    
    # Now try importing
    print("\nTrying import...")
    import agent.product_management_agent as pma
    print("Import successful!")
    
    # Check for the class
    print(f"\nChecking for class...")
    if hasattr(pma, 'SemanticKernelProductManagementAgent'):
        print("✓ Class found!")
    else:
        print("✗ Class NOT found")
        print(f"Available classes: {[n for n in dir(pma) if isinstance(getattr(pma, n, None), type)]}")
        
except SyntaxError as e:
    print(f"Syntax Error: {e}")
    traceback.print_exc()
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
    traceback.print_exc()
