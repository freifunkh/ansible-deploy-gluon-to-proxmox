#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return { 'mac2ipv6': self.mac2ipv6 }

    def mac2ipv6(self, mac):
        # only accept MACs separated by a colon
        parts = mac.split(":")

        # modify parts to match IPv6 value
        parts.insert(3, "ff")
        parts.insert(4, "fe")
        parts[0] = "%x" % (int(parts[0], 16) ^ 2)

        # format output
        ipv6Parts = []
        for i in range(0, len(parts), 2):
            ipv6Parts.append("".join(parts[i:i+2]))
        ipv6 = "fe80::%s" % (":".join(ipv6Parts))
        return ipv6
