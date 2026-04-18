from mininet.topo import Topo

class OrangeTopo(Topo):
    def build(self):
        # Create a single switch
        s1 = self.addSwitch('s1')

        # Create three hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')

        # Connect them all to the switch
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)

topos = {'orangetopo': (lambda: OrangeTopo())}