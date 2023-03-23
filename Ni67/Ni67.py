import kshell_utilities as ksutil
import matplotlib.pyplot as plt

ksutil.latex_plot()
ksutil.flags["debug"] = True

BIN_WIDTH = 0.2
EX_MIN = 5  # Adjust this to match the lower experimental excitation energy.
EX_MAX = 50 # I usually set this to S(n), but that value is very low for this neutron rich nucleus.

def main():
    Ni67 = ksutil.loadtxt(path="gs8/200_levels/1hw/summary_Ni67_gs8_000.txt")

    # Ni67.angular_momentum_distribution_plot(
    #     bin_width = 1,
    #     E_min = 0,
    #     E_max = 20
    # )

    Ni67.level_plot(filter_parity="both")
    Ni67.nld()

    fig, ax = plt.subplots()

    bins, gsf_M1 = Ni67.gsf(
        bin_width = BIN_WIDTH,
        Ex_min = EX_MIN,
        Ex_max = EX_MAX,
        multipole_type = "M1",
        plot = False
    )
    bins, gsf_E1 = Ni67.gsf(
        bin_width = BIN_WIDTH,
        Ex_min = EX_MIN,
        Ex_max = EX_MAX,
        multipole_type = "E1",
        plot = False
    )
    ax.step(bins, (gsf_M1 + gsf_E1), label=r"SM $E1 + M1$", color="grey")
    ax.step(bins, gsf_M1, label=r"SM $M1$", color="red")
    ax.step(bins, gsf_E1, label=r"SM $E1$", color="blue")

    ax.set_yscale('log')
    ax.set_xlabel(r"E$_{\gamma}$ [MeV]")
    ax.set_ylabel(r"GSF [MeV$^{-3}$]")
    ax.set_title(r"$^{67}$Ni, gs8, 200 levels per $j^{\pi}$, $1 \hbar \omega$")
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()