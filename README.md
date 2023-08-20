# Fast_Port_Scanner

This Project is about port scanning in fastest way with port number and their service . use this to find out of open ports.

#Explanation_of_code_Here :::-----

The main function serves as the entry point of the script. It defines the target (host) to scan and the port_range (range of ports) to scan.

The num_threads variable specifies the number of concurrent threads to use for scanning. This is where you can adjust the level of concurrency based on your system's capabilities.

The concurrent.futures.ThreadPoolExecutor context manager is used to create a thread pool with the specified number of workers (threads). It manages the thread pool efficiently, and the with block ensures that resources are released properly when done.

Inside the context, a list comprehension creates a list of futures by submitting tasks (port scans) to the executor using executor.submit(scan_port, target, port) for each port in the range.

Finally, concurrent.futures.wait(futures) waits for all tasks (futures) to complete before the program finishes.

By combining thread pooling with asynchronous execution, the code effectively scans multiple ports concurrently, allowing for faster scanning of a wide range of ports.

In this code, I've added a dictionary named PORT_TO_SERVICE that maps commonly used port numbers to their corresponding service names. You can extend this dictionary by adding more port numbers and their associated service names.

Inside the scan_port function, after detecting that a port is open, we use the PORT_TO_SERVICE.get(port, "Unknown") line to retrieve the service name associated with the port from the dictionary. If the port is not found in the dictionary, it defaults to "Unknown".

The output includes the port number and its associated service name, providing more context about the open ports. This can be helpful in identifying the services that are running on those ports.
