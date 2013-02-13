class Dev(object):

    def render_to_response(self, context, **response_kwargs):
        print "****************"
        print "context items:\n"
        for k, v in context.items():
            print "** %s **: %s\n" % (k, v)
        return super(Dev, self).render_to_response(context, **response_kwargs)

    # def dispatch(self, request, *args, **kwargs):
    #     print "****************"
    #     print "Raw HTTP request:"
    #     print "****************"
    #     print request.body
    #     print "****************"
    #     return super(Dev, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print "**********"
        print "POST items:\n"
        for k, v in request.POST.items():
            print "* %s: %s\n" % (k, v)
        return super(Dev, self).post(request, *args, **kwargs)