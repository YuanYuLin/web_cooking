var gulp = require('gulp');
var concat = require('gulp-concat');
var pump = require('pump')

gulp.task('concat_js', function(cb) {
    pump([
        gulp.src([
{% for gulp in GULPFILE %} {% if loop.last %}
        'app/js/{{gulp}}'
{% else %}
        'app/js/{{gulp}}',
{% endif %}{% endfor %}
        ]),
	concat('app.js'),
	gulp.dest('app')
    ], cb);
});

gulp.task('concat_css', function(cb) {
    pump([
        gulp.src([
        'app/css/*.css'
        ]),
	concat('app.css'),
	gulp.dest('app')
    ], cb);
});


