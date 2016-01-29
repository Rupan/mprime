GIMPS (mprime) packaging for RPM-based Linux distributions
----------------------------------------------------------

This repository hosts RPM SPEC files and associated items required in order
to build mprime RPMs from either the "source" ZIP file (which contains much
proprietary / closed code itself) or the binary tarballs.

Building on RHEL
----------------

These RPM SPECs have been tested on 64-bit RHEL 7.  They will likely work
on older versions of RHEL as well as SUSE, Mandriva, etc but have not been
tested on those systems.  Patches are welcome.

You'll need an appropriately-configured development environment:

    # sudo yum install libstdc++devel libcurl-devel rpmdevtools
    # sudo yum groupinstall 'Development Tools'

Then you'll need to fetch the source material before you can proceed with
the standard build process.  Note that the "source" build (i.e., using
mprime-src.spec) still requires the binary distributions since these contain
the mprime documentation.

    # ./download-sources.sh
    # rpmbuild -bb SPECS/mprime-src.spec
    # rpmbuild -bb SPECS/mprime-bin.spec

The "source" build will not work with Primenet (but the binary one will).
