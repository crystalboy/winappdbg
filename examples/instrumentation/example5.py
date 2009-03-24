# Example #5
# http://code.google.com/p/python-winappdbg/wiki/Instrumentation#Example_#5:_reading_the_process_memory

from winappdbg import Process

def process_read( pid, address, length ):
    
    # Instance a Process object
    process = Process( pid )
    
    # Read the process memory
    data = process.read( address, length )
    
    # Return a Python string with the memory contents
    return data

# When invoked from the command line,
# the first argument is a process ID,
# the second argument is a remote pointer (in hexadecimal),
# the third argument is a size in bytes
if __name__ == "__main__":
    import sys
    pid     = int( sys.argv[1] )
    address = int( sys.argv[2], 0x10 )
    length  = int( sys.argv[3] )
    print "%r" % process_read( pid, address, length )
