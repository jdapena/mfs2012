from gi.repository import Gtk

def N_(message) : return message

MENU_UI = '''
<ui>
    <menubar name="MenuBar">
        <menu action="TraktorMenu">
            <menuitem action="About" />
        </menu>
    </menubar>
</ui>
'''

class TraktorWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title('Traktor')
        self.set_size_request(500, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(box)

        self.store = Gtk.ListStore(int, str, str)

        view = Gtk.TreeView(self.store)

        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn(_('Title'), renderer, text=1)
        view.append_column(column)

        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn(_('Description'), renderer, text=2)
        view.append_column(column)

        view.connect('row-activated', self._on_row_activated)


        self.ui_manager = self._setup_ui_manager()
        menu_bar = self.ui_manager.get_widget('/MenuBar')
        box.pack_start(menu_bar, False, False, 0)
        box.add(view)

        self._update_list()

        self.connect('delete-event', self._quit)

    def _update_list(self):
        self.store.append([0, 'Cars', 'A red car...'])
        self.store.append([1, 'Toy Story', 'Buzz and Buddy...'])
        self.store.append([2, 'Up', 'A house with baloons...'])


    def _setup_ui_manager(self):
        ui_manager = Gtk.UIManager()
        ui_manager.add_ui_from_string(MENU_UI)
        accel_group = ui_manager.get_accel_group()
        self.add_accel_group(accel_group)
        action_group = Gtk.ActionGroup('Actions')
        action_group.set_translation_domain(None)
        action_group.add_actions([
                ('TraktorMenu', None, N_('_Traktor'), None, None, None),
                ('About', Gtk.STOCK_ABOUT,
                 N_('_About'), None, N_('About this application'),
                 self._on_about_action),
                ])
        ui_manager.insert_action_group(action_group)
        return ui_manager

    def _on_about_action(self, action):
        about = Gtk.AboutDialog()
        about.set_program_name(_("Traktor"))
        about.run()
        about.destroy()

    def _on_row_activated(self, tree_view, path, column):
        item = tree_view.get_model().get_iter(path)
        print _('Title:'), tree_view.get_model().get_value(item, 1)

    def _quit(self, window, event):
        Gtk.main_quit()

    def run(self):
        self.show_all()
        Gtk.main()
