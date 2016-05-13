# -*- encoding: utf-8 -*-

from vulyk.app import app

if __name__ == '__main__':
    app.config.from_object('local_settings')
    app.run()
