function fader(parent) {
    var self = {current: 0,
                items: parent.children()};
    parent.css('position', 'relative');
    function refresh() {
        self.items = parent.children();
        self.items.hide();
        self.items.eq(self.current).show();
        self.items.css({'position':'absolute',
                        'top':0,
                        'left':0});
    }
    function fade_to(index, callback) {
        if (index==self.current) return;
        var now = self.items.eq(self.current);
        now.css('z-index',1);
        self.items.eq(index).css('z-index',0).show();
        now.fadeOut(callback);
        self.current = index;
    }
    function slideshow(delay) {
        var next = self.current+1;
        if (next >= self.items.length) next=0;
        function callback() {
            setTimeout(function() {self.slideshow(delay)}, delay);
        }
        self.fade_to(next, callback);
    }
    self.fade_to = fade_to;
    self.slideshow = slideshow;
    self.refresh = refresh;
    refresh();
    return self;
}
