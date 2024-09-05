import matplotlib.pyplot as plt
import numpy as np
import kshell_utilities as ksutil
ksutil.latex_plot()
ksutil.flags['debug'] = True

# [MeV]
BIN_WIDTH = 0.2
EX_MIN = 4  # Default value. Set this to be larger than the discrete region.
EX_MAX = 10 # Default value. Set this to the neutron separation energy.

def main():
    res = ksutil.loadtxt(
        path = 'snbg1/200_levels/',
        load_and_save_to_file = True,
    )
    bins_nld, density, counts = res.nld(
        return_counts = True,
        plot = False,
    )

    j_values = np.unique(res.levels[:, 1])

    print("jp     N levels")
    for j in j_values:
        print(f"{j}+    {len(res.levels[np.logical_and(res.levels[:, 1] == j, res.levels[:, 2] == +1)])}")
        print(f"{j}-    {len(res.levels[np.logical_and(res.levels[:, 1] == j, res.levels[:, 2] == -1)])}")

    fig_1, ax_1 = plt.subplots()
    ax_1.step(bins_nld, density)
    ax_1.set_ylabel(r"NLD [MeV$^{-1}$]")
    ax_1.set_xlabel("E [MeV]")
    plt.show()

    fig_2, ax_2 = plt.subplots()

    ax_2.step(bins_nld, counts)
    ax_2.set_ylabel(r"Counts")
    ax_1.set_xlabel("E [MeV]")
    plt.show()

    fig_0, ax_0 = plt.subplots()
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
    ax_0.step(bins, gsf, label=r'SM $E1 + M1$', color='grey')
    ax_0.step(bins, gsf_M1, label=r'SM $M1$', color='red')
    ax_0.step(bins, gsf_E1, label=r'SM $E1$', color='blue')

    ax_0.set_yscale('log')
    ax_0.set_xlabel(r'E$_{\gamma}$ [MeV]')
    ax_0.set_ylabel(r'$f(E_{\gamma})$ [MeV$^{-3}$]')
    # ax_0.set_ylabel(r'GSF [MeV$^{-3}$]')
    ax_0.legend()
    # fig_0.savefig('gsf.png', dpi=600)
    plt.show()

if __name__ == '__main__':
    main()