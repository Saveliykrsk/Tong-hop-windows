sudo cpulimit -l 80 -- sudo kvm -daemonize \
    -cpu host,+topoext,hv_relaxed,hv_spinlocks=0x1fff,hv-passthrough,+pae,+nx,kvm=on,+svm \
    -smp 2,cores=2 \
    -M q35,usb=on \
    -device usb-tablet \
    -m 8G \
    -device virtio-balloon-pci \
    -vga virtio \
    -net nic,netdev=n0,model=virtio-net-pci \
    -netdev user,id=n0,hostfwd=tcp::3389-:3389 \
    -boot c \
    -device virtio-serial-pci \
    -device virtio-rng-pci \
    -enable-kvm \
    -drive file=/mnt/a.qcow2 \
    -drive if=pflash,format=raw,readonly=off,file=/usr/share/ovmf/OVMF.fd \
    -uuid e47ddb84-fb4d-46f9-b531-14bb15156336 \
    -soundhw hda \
    -chardev spicevmc,id=vdagent,name=vdagent \
    -device virtserialport,chardev=vdagent,name=com.redhat.spice.0
