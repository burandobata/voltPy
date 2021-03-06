from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from manager.exceptions import VoltPyNotAllowed, VoltPyDoesNotExists
import manager.plotmanager as mpm
import manager.forms as mforms
import collections

def voltpy_render(*args, **kwargs):
    """
    This is proxy function which sets usually needed context elemenets.
    It is very much prefered over django default.
    """
    request = kwargs['request']
    context = kwargs.pop('context', {})
    con_scr = context.get('scripts','')
    scr = ''.join([
        mpm.PlotManager.required_scripts,
        "\n",
        con_scr,
    ])
    context['scripts'] = scr
    context['plot_width'] = mpm.PlotManager.plot_width
    context['plot_height'] = mpm.PlotManager.plot_height
    notifications = request.session.pop('VOLTPY_notification', [])
    if ( len(notifications) > 0 ):
        con_note = context.get('notifications',[])
        con_note.extend(notifications)
        context['notifications'] = con_note
        return render(*args, **kwargs, context=context)
    else:
        return render(*args, **kwargs, context=context)

def add_notification(request, text, severity=0):
    notifications = request.session.get('VOLTPY_notification', [])
    notifications.append( {'text': text, 'severity':severity} )
    request.session['VOLTPY_notification'] = notifications

def delete_generic(request, user, item):
    """
    The generic function to which offers ability to delete
    model istance with user confirmation.
    """
    if item == None:
        return HttpResponseRedirect(
            reverse('index', args=[user.id])
        )

    itemclass = str(item.__class__.__name__)
    if not item.canBeUpdatedBy(user):
        raise VoltPyNotAllowed(user)
    if request.method == 'POST':
        form = mforms.DeleteForm(item, request.POST)
        if form.is_valid():
            a = form.process(user, item)
            if a:
                return HttpResponseRedirect(
                    reverse('browse'+itemclass, args=[user.id])
                )
    else:
        form = mforms.DeleteForm(item)

    context = { 
        'scripts': mpm.PlotManager.required_scripts,
        'form': form,
        'item': item,
        'user': user
    }
    return voltpy_render(
        request=request, 
        template_name='manager/deleteGeneric.html',
        context=context
    )

def generate_plot(request, user, plot_type, value_id, **kwargs):
    allowedTypes = [
        'file',
        'analysis',
        'curveset',
        'curves'
    ]
    if not ( plot_type in allowedTypes ):
        return
    vtype = kwargs.get('vtype', plot_type)
    vid = kwargs.get('vid', value_id)
    addTo = kwargs.get('add', None)

    pm = mpm.PlotManager()
    data=[]
    if (plot_type == 'file' ):
        data=pm.fileHelper(user, value_id)
        pm.xlabel = pm.xLabelHelper(user)
        pm.include_x_switch = True
    elif (plot_type == 'curveset'):
        data=pm.curveSetHelper(user, value_id)
        pm.xlabel = pm.xLabelHelper(user)
        pm.include_x_switch = True
    elif (plot_type == 'analysis'):
        data=pm.analysisHelper(user, value_id)
        xlabel = pm.xLabelHelper(user)
        pm.include_x_switch = False
    elif (plot_type == 'curves'):
        data=pm.curvesHelper(user, value_id)
        pm.xlabel = pm.xLabelHelper(user)
        pm.include_x_switch = True


    pm.ylabel = 'i / µA'
    pm.setInteraction(kwargs.get('interactionName', 'none'))

    for d in data:
        pm.add(**d)

    if addTo:
        for a in addTo:
            pm.add(**a)

    return pm.getEmbeded(request, user, vtype, vid) 
