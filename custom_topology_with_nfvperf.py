from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink

def customTopo():
    net = Mininet(controller=RemoteController, switch=OVSSwitch, link=TCLink)

    # Add a remote controller
    controller_ip = '192.168.182.135'
    c0 = net.addController('c0', controller=RemoteController, ip=controller_ip, port=6653)

    # Add a switch
    s1 = net.addSwitch('s1')

    # Add hosts
    h1 = net.addHost('h1', ip='10.0.0.1')
    h2 = net.addHost('h2', ip='10.0.0.2')

    # Add links between switch and hosts
    net.addLink(h1, s1)
    net.addLink(h2, s1)

    # Start the network
    net.start()

    # Set controller for the switch
    s1.start([c0])

    # Install and configure NFVPerf on host1
    setup_nfvperf_on_host(h1)

    # Launch the CLI
    CLI(net)

    # Stop the network
    net.stop()

def setup_nfvperf_on_host(host):
    """ Install and configure NFVPerf on a given Mininet host """
    # Install required packages (example for Ubuntu)
    host.cmd('apt-get update')
    host.cmd('apt-get install -y python3 python3-pip')
    host.cmd('pip3 install nfvperf')  # Adjust the package name if needed

    # Create a configuration file for NFVPerf
    config_content = """
    latency:
      tool: ping
      parameters:
        - -c 10
        - -i 0.5

    packet_loss:
      tool: ping
      parameters:
        - -c 100
        - -i 1

    throughput:
      tool: iperf
      parameters:
        - -c 10.0.0.2
        - -t 10
    """
    config_path = '/tmp/nfvperf_config.yaml'
    host.cmd(f'echo "{config_content}" > {config_path}')

    # Start NFVPerf with the configuration
    host.cmd(f'nfvperf --config {config_path} --host h1 --target 10.0.0.2 &')

if __name__ == '__main__':
    setLogLevel('info')
    customTopo()
