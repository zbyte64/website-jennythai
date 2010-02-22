COMPRESS = True
COMPRESS_VERSION = True
COMPRESS_CSS = {
    'main' : {
        'source_filenames': ['css/main.css'],
        'output_filename': 'c/main.r?.css'
    },
    'gallery_list' : {
        'source_filenames': ['css/gallery_list.css'],
        'output_filename': 'c/gallery_list.r?.css'
    },
    'gallery_detail' : {
        'source_filenames': ['css/gallery_detail.css'],
        'output_filename': 'c/gallery_detail.r?.css'
    },
    'blog' : {
        'source_filenames': ['css/blog.css'],
        'output_filename': 'c/blog.r?.css'
    },
}

COMPRESS_JS = {
    #'main' : {
    #    'source_filenames': [],
    #    'output_filename': 'c/main.r?.js'
    #},
    'gallery_list' : {
        'source_filenames': ['js/gallery_list.js'],
        'output_filename': 'c/gallery_list.r?.js'
    },
    'gallery_detail' : {
        'source_filenames': ['js/gallery_detail.js'],
        'output_filename': 'c/gallery_detail.r?.js'
    },
}
