from hyperadmin.mediatypes.html5 import Html5MediaType

class AdminHtml5MediaType(Html5MediaType):
    default_namespace = 'adminhtmlclient'
    template_name = 'hyperadminclient/resource.html'
    template_dir_name = 'hyperadminclient'
    
    def get_context_data(self, link, state):
        context = super(AdminHtml5MediaType, self).get_context_data(link, state)
        links = state.get_outbound_links()
        tool_links = [link for link in links if link.rel != 'breadcrumb']
        #TODO convert into template tag
        context['tool_links'] = list()
        for link in tool_links:
            if link.is_simple_link and link.form_class:
                context['tool_links'].append({'links':link.clone_into_links(), 'dropdown':True, 'prompt':link.prompt})
            else:
                context['tool_links'].append({'link':link, 'dropdown':False})
        context['breadcrumbs'] = [link for link in links if link.rel == 'breadcrumb']
        return context
    
    def get_change_list_context_data(self, link, state, context):
        links = state.get_templated_queries()
        context['pagination_links'] = [link for link in links if link.rel == 'pagination']
        filter_links = dict()
        for link in links :
            if link.rel == 'filter':
                section = link.cl_headers.get('group', link.prompt)
                filter_links.setdefault(section, [])
                filter_links[section].append(link)
        context['filter_links'] = filter_links
        return context
        
