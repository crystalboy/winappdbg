# Example #9
# http://code.google.com/p/python-winappdbg/wiki/Instrumentation#Example_#9:_print_a_thread&#x27;s_code_disassembly

from winappdbg import Thread, CrashDump, System

def print_thread_disassembly( tid ):
    
    # Request debug privileges
    System.request_debug_privileges()
    
    # Instance a Thread object
    thread = Thread( tid )
    
    # Suspend the thread execution
    thread.suspend()
    
    # Get the thread's currently running code
    try:
        eip  = thread.get_pc()
        code = thread.disassemble_around( eip )
    
    # Resume the thread execution
    finally:
        thread.resume()
    
    # Display the thread context
    print
    print CrashDump.dump_code( code, eip ),

# When invoked from the command line,
# the first argument is a thread ID
if __name__ == "__main__":
    import sys
    tid = int( sys.argv[1] )
    print_thread_disassembly( tid )
