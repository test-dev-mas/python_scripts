import gi
import usb.core

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class ComboBoxWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Automated Testing")

        vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.add(vbox)

        self.set_border_width(10)

        self.button = Gtk.Button(label="Find Device")
        self.button.connect("clicked", self.on_button_clicked)
        vbox.pack_start(self.button, False, False, 0)

        self.name_store = Gtk.ListStore(int, str)
        
        name_combo = Gtk.ComboBox.new_with_model_and_entry(self.name_store)
        # name_combo.connect("changed", self.on_name_combo_changed)
        name_combo.set_entry_text_column(1)
        vbox.pack_start(name_combo, False, False, 0)

    def on_button_clicked(self, widget):
        # dev = usb.core.find(idVendor=0x5345, idProduct=0x1234)
        # dev.reset()

        # dev.write(0x01, b'*IDN')
        # res=dev.read(0x81,64,1000)
        # id=res.tobytes().decode('utf-8')
        # # print(id.split(","))

        # self.name_store.append([1, id])
        self.name_store.clear()
        dev=usb.core.find(find_all=True)
        for id,device in enumerate(dev):
            # usb.util.get_string(device,128,device.idVendor)
            self.name_store.append([id,device._str()+device.manufacturer+device.product])

    def on_name_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            row_id, name = model[tree_iter][:2]
            print("Selected: ID=%d, name=%s" % (row_id, name))
        else:
            entry = combo.get_child()
            print("Entered: %s" % entry.get_text())



win = ComboBoxWindow()
# win.set_size_request(500,500)
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()