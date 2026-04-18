from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class OrangeFirewall (object):
  def __init__ (self):
    core.openflow.addListeners(self)

  def _handle_PacketIn (self, event):
    packet = event.parsed
    if not packet.parsed: return

    # Check for IPv4 packets
    ip = packet.find('ipv4')
    if ip:
        # SCENARIO: Block Host 1 (10.0.0.1) from talking to Host 2 (10.0.0.2)
        # This fulfills the "Rule-based filtering" requirement
        if ip.srcip == "10.0.0.1" and ip.dstip == "10.0.0.2":
            log.info("--- FIREWALL: Dropping packet from %s to %s ---" % (ip.srcip, ip.dstip))
            return # Dropping the packet by not sending any OpenFlow actions

    # Standard "Match-Action": Flood the packet if not blocked
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
    event.connection.send(msg)

def launch ():
  core.registerNew(OrangeFirewall)