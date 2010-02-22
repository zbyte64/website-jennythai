from django.views.generic.list_detail import object_list

def blogentrytag_list(request, tagname):
    queryset = BlogEntry.objects.tagged(tagname) & BlogEntry.objects.live()
    return object_list(request, queryset=queryset)
