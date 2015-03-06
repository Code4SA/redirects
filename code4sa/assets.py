from django_assets import Bundle, register

register('css', Bundle(
    # list 3rd party and raw css here
    #'bower_components/bootstrap/dist/css/bootstrap.min.css',
    #'bower_components/bootstrap/dist/css/bootstrap-theme.min.css',
    #'bower_components/fontawesome/css/font-awesome.css',
    Bundle(
        # list SCSS files here
        'stylesheets/app.scss',
        filters='pyscss',
        output='css/styles.%(version)s.css'),
    output='css/app.%(version)s.css'))

register('js', Bundle(
    # list JS files here
    'javascript/app.js',
    output='js/app.%(version)s.js'))