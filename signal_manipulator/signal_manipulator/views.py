import numpy as np

from django.shortcuts import render

from .chart_helper import \
    cos_signal, impulse, sin_signal, step, \
    stem, stem2, plot, plot2



def signal(request):
    context = {}
    ts, cos_sig = cos_signal(freq=10, amp=1)
    cos_sig_scaled = 3 * cos_sig
    context['graph'] = plot2(t=ts, y1=cos_sig, y2=cos_sig_scaled, label1="Cos Signal", label2="Scaled Cos Signal")
    return render(request, 'signal.html', context=context)


def cos_view(request):
    context = {}
    if request.method == 'POST':
        data = request.POST
        action = str(data.get('action_type'))
        if action == 'GENERATE':
            amp = int(data.get('amplitude'))
            freq = int(data.get('frequency'))
            request.session['cos_amp'] = amp
            request.session['cos_freq'] = freq
            ts, cos_sig = cos_signal(freq, amp)
            graph = plot(ts, cos_sig, "Cos Signal")
            context['graph'] = graph
            return render(request, 'cos_signal.html', context=context)
        elif action == 'SCALE':
            scale_fac = int(data.get('scale_factor'))
            amp = request.session['cos_amp']
            freq = request.session['cos_freq']
            ts, cos_sig = cos_signal(freq, amp)
            cos_sig_scaled = scale_fac * cos_sig
            graph = plot2(ts, cos_sig, cos_sig_scaled, "Cos Signal", f"Cos Signal Scaled({scale_fac})")
            context['graph'] = graph
            return render(request, 'cos_signal.html', context=context)
    if request.session.get('cos_freq') and request.session.get('cos_amp'):
        amp = request.session['cos_amp']
        freq = request.session['cos_freq']
        ts, cos_sig = cos_signal(freq, amp)
        graph = plot(ts, cos_sig, "Cos Signal")
        context['graph'] = graph
    return render(request, 'cos_signal.html', context=context)


def sin_view(request):
    context = {}
    if request.method == 'POST':
        data = request.POST
        action = str(data.get('action_type'))
        print(action)
        if action == 'GENERATE':
            amp = int(data.get('amplitude'))
            freq = int(data.get('frequency'))
            request.session['sin_amp'] = amp
            request.session['sin_freq'] = freq
            ts, sin_sig = sin_signal(freq, amp)
            graph = plot(ts, sin_sig, "Sin Signal")
            context['graph'] = graph
            return render(request, 'sin_signal.html', context=context)
        elif action == 'SCALE':
            scale_fac = int(data.get('scale_factor'))
            print(data)
            amp = request.session['sin_amp']
            freq = request.session['sin_freq']
            ts, sin_sig = sin_signal(freq, amp)
            sin_sig_scaled = scale_fac * sin_sig
            graph = plot2(ts, sin_sig, sin_sig_scaled, "Cos Signal", f"Cos Signal Scaled({scale_fac})")
            context['graph'] = graph
            return render(request, 'sin_signal.html', context=context)
    if request.session.get('sin_freq') and request.session.get('sin_amp'):
        amp = request.session['sin_amp']
        freq = request.session['sin_freq']
        ts, sin_sig = sin_signal(freq, amp)
        graph = plot(ts, sin_sig, "Sin Signal")
        context['graph'] = graph
    return render(request, 'sin_signal.html', context=context)


def step_view(request):
    context = {}
    ts = np.arange(-10, 10, 0.01)
    step_sig = step(ts)
    if request.method == 'POST':
        data = request.POST
        action = str(data.get('action_type'))
        if action == 'TIME_SHIFT':
            shift = int(data.get('shift'))
            time_sh_step = step(ts + shift)
            graph = plot2(ts, step_sig, time_sh_step, "Unit Step Signal", f"Time Shifted Unit Step Signal({shift})")
            context['graph'] = graph
            return render(request, 'step_signal.html', context=context)
        elif action == 'TIME_REVERSAL':
            rev_step_signal = step(-ts)
            graph = plot2(ts, step_sig, rev_step_signal, "Unit Step Signal", "Unit Step Signal Reversed")
            context['graph'] = graph
            return render(request, 'step_signal.html', context=context)
    graph = plot(ts, step_sig, "Unit Step Signal")
    context['graph'] = graph
    return render(request, 'step_signal.html', context=context)


def impulse_view(request):
    ts = np.arange(-10, 10, 1)
    impulse_sig = impulse(ts)
    context = {}
    if request.method == 'POST':
        data = request.POST
        shift = int(data.get('shift'))
        impulse_sig_shifted = impulse(ts + shift)
        graph = stem2(ts, impulse_sig, impulse_sig_shifted, "Original Impulse Signal", "Time Shifted Impulse Signal")
        context['graph'] = graph
        return render(request, 'impulse_signal.html', context=context)
    graph = stem(ts, impulse_sig, 'Impulse Signal')
    context['graph'] = graph
    return render(request, 'impulse_signal.html', context=context)
