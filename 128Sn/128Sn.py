import matplotlib.pyplot as plt
import kshell_utilities as ksutil
ksutil.latex_plot()
ksutil.flags['debug'] = True

# [MeV]
BIN_WIDTH = 0.2
EX_MIN = 4  # Default value. Set this to be larger than the discrete region.
EX_MAX = 10 # Default value. Set this to the neutron separation energy.

def main():
    fig, ax = plt.subplots()

    res = ksutil.loadtxt(
        path = 'snbg1/200_levels/',
        load_and_save_to_file = True,
    )
    # res.nld()
    bins, gsf_E1, n_transitions, included_transitions = res.gsf(
        bin_width = BIN_WIDTH,
        Ex_min = EX_MIN,
        Ex_max = EX_MAX,
        multipole_type = 'E1',
        plot = False,
    )
    bins_M1, gsf_M1, n_transitions, included_transitions = res.gsf(
        bin_width = BIN_WIDTH,
        Ex_min = EX_MIN,
        Ex_max = EX_MAX,
        multipole_type = 'M1',
        plot = False
    )
    gsf = gsf_E1 + gsf_M1
    ax.step(bins, gsf, label=r'SM $E1 + M1$', color='grey')
    ax.step(bins, gsf_M1, label=r'SM $M1$', color='red')
    ax.step(bins, gsf_E1, label=r'SM $E1$', color='blue')

    ax.set_yscale('log')
    ax.set_xlabel(r'E$_{\gamma}$ [MeV]')
    ax.set_ylabel(r'$f(E_{\gamma})$ [MeV$^{-3}$]')
    # ax.set_ylabel(r'GSF [MeV$^{-3}$]')
    ax.legend()
    # fig.savefig('gsf.png', dpi=600)
    plt.show()

if __name__ == '__main__':
    main()