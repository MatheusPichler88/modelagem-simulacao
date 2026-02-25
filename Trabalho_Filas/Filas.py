
import Calculadora_EarlingC as calc

"""Definindo as funções para calculos das métricas M/M/c baseadas em Erlang C"""
import Calculadora_EarlingC as calc

def utilizacao(a, c):
    return a / c

def tempo_espera_fila(P_wait, c, mu, lam):
    return P_wait / (c * mu - lam)

def num_medio_fila(lam, Wq):
    return lam * Wq

def tempo_medio_sistema(Wq, mu):
    return Wq + 1 / mu

def num_medio_sistema(lam, W):
    return lam * W

def calcular_metricas_mmc(a, c, lam=None, mu=None):
    P_wait = calc.erlang_c(a, c)

    """ Calcula as métricas do sistema M/M/c baseado no tráfego oferecido a=λ/μ (Erlangs) e c servidores.
        Se λ e μ forem fornecidos, calcula todas as métricas; caso contrário, retorna apenas P(wait)."""
    if a >= c:
        return {
            'P_wait': 1.0,
            'utilizacao': a/c,
            'Wq': float('inf'),
            'Lq': float('inf'),
            'W': float('inf'),
            'L': float('inf'),
            'estavel': False
        }
    
    if lam is None or mu is None:
        return {
            'P_wait': P_wait,
            'utilizacao': utilizacao(a, c),
            'Wq': None,
            'Lq': None,
            'W': None,
            'L': None,
            'estavel': True
        }
    
    rho = utilizacao(a, c)
    Wq = tempo_espera_fila(P_wait, c, mu, lam)
    Lq = num_medio_fila(lam, Wq)
    W = tempo_medio_sistema(Wq, mu)
    L = num_medio_sistema(lam, W)
    
    return {
        'P_wait': P_wait,
        'utilizacao': rho,
        'Wq': Wq,
        'Lq': Lq,
        'W': W,
        'L': L,
        'estavel': True
    }

