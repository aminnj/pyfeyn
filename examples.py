import ROOT
from pyfeyn import (
    Label,
    Marker,
    Vertex,
    Propagator,
    init_diagram,
    draw_grid,
    save_diagram,
)
import os


def diag1():
    vep = Vertex(20, 35, label=Label("e^{+}", offsetx=-2, offsety=-2))
    vem = Vertex(20, 65, label=Label("e^{-}", offsetx=-2, offsety=2))
    veebl = Vertex(35, 50)
    veebr = Vertex(65, 50)
    vqp = Vertex(80, 35, label=Label("q", offsetx=2, offsety=-2))
    vqm = Vertex(80, 65, label=Label("#bar{q}", offsetx=2, offsety=2))

    init_diagram()

    Propagator(vep, veebl, typ="line", fliparrow=True).draw()
    Propagator(vem, veebl, typ="line").draw()
    Propagator(
        veebl,
        veebr,
        typ="wavyline",
        label=Label("Z^{0}/#gamma", offsety=6),
        linecolor=ROOT.kBlue + 2,
    ).draw()

    Propagator(vqp, veebr, typ="line").draw()
    Propagator(vqm, veebr, typ="line", fliparrow=True).draw()

    vgluonl = Vertex(65 + 7.5, 50 + 7.5)
    vgluonr = Vertex(65 + 7.5 + 7.5 + 4, 50 - 4, Label("g", offsetx=2, offsety=2))

    Propagator(vgluonl, vgluonr, typ="curlyline").draw()

    Label("e^+e^-\\rightarrow q\\bar{q}g", 50, 30, textsize=0.07).draw()

    save_diagram("feynmandiagram_eetoqq.pdf")
    os.system("ic feynmandiagram_eetoqq.pdf")


def diag2():

    vg1 = Vertex(20, 60, label=Label("g", offsetx=-2))
    vg2 = Vertex(20, 30, label=Label("g", offsetx=-2))
    vg1t = Vertex(45, 60)
    vg2t = Vertex(45, 30)
    vg1t_right = Vertex(70, 60, label=Label("t", offsetx=2))
    vg2t_right = Vertex(70, 30, label=Label("t", offsetx=2))
    vtth = Vertex(45, 45)
    vh_right = Vertex(70, 45, label=Label("H(A)", offsetx=5))

    init_diagram()

    Propagator(vg1, vg1t, typ="curlyline").draw()
    Propagator(vg2, vg2t, typ="curlyline").draw()
    Propagator(
        vtth, vg1t, typ="line", label=Label("t", offsetx=-2), linecolor=ROOT.kRed - 4
    ).draw()
    Propagator(
        vtth,
        vg2t,
        typ="line",
        label=Label("t", offsetx=-2),
        linecolor=ROOT.kRed - 4,
        fliparrow=True,
    ).draw()
    Propagator(vg1t, vg1t_right, typ="line", linecolor=ROOT.kRed - 4).draw()
    Propagator(
        vg2t, vg2t_right, typ="line", linecolor=ROOT.kRed - 4, fliparrow=True
    ).draw()
    Propagator(vtth, vh_right, typ="dashedline", linecolor=ROOT.kAzure - 6).draw()

    save_diagram("feynmandiagram_tth.pdf")
    os.system("ic feynmandiagram_tth.pdf")


def diag3():
    v_h = Vertex(10, 45, label=Label("#rm{H}", offsetx=-4))
    v_hzz = Vertex(50, 45, marker=Marker(color=ROOT.kBlack))
    v_zll = Vertex(70, 70)
    v_eps = Vertex(
        60,
        32.5,
        marker=Marker(color=ROOT.kGray + 2),
        label=Label("#epsilon", offsetx=-4, offsety=-4),
    )
    v_zdll = Vertex(70, 20)
    v_zl1 = Vertex(90, 80, label=Label("#rm{#ell}", offsetx=2))
    v_zl2 = Vertex(90, 60, label=Label("#rm{#bar{#ell}}", offsetx=2))
    v_zdl1 = Vertex(90, 30, label=Label("#rm{#ell}", offsetx=2))
    v_zdl2 = Vertex(90, 10, label=Label("#rm{#bar{#ell}}", offsetx=2))

    init_diagram()

    Propagator(v_h, v_hzz, typ="dashedline", noarrow=True).draw()

    Propagator(
        v_hzz, v_zll, typ="wavyline", label=Label("#rm{Z}", offsetx=-5, offsety=4)
    ).draw()
    Propagator(
        v_hzz, v_eps, typ="wavyline", label=Label("#rm{Z}", offsetx=5, offsety=4)
    ).draw()
    Propagator(
        v_eps, v_zdll, typ="wavyline", label=Label("#rm{Z_D}", offsetx=5, offsety=4)
    ).draw()

    Propagator(v_zll, v_zl1, typ="line").draw()
    Propagator(v_zll, v_zl2, typ="line", fliparrow=True).draw()
    Propagator(v_zdll, v_zdl1, typ="line").draw()
    Propagator(v_zdll, v_zdl2, typ="line", fliparrow=True).draw()

    save_diagram("feynmandiagram_hzzd.pdf")
    os.system("ic feynmandiagram_hzzd.pdf")


def diag4():
    init_diagram()

    v_bleft = Vertex(15, 40, label=Label(r"\bar{\mathrm{b}}", offsetx=-3))
    v_vtb = Vertex(37, 40, marker=Marker(color=ROOT.kBlack, radius=0.8))
    Propagator(v_bleft, v_vtb, typ="line", fliparrow=True).draw()

    v_vts = Vertex(63, 40, marker=Marker(color=ROOT.kBlack, radius=0.8))
    v_sright = Vertex(85, 40, label=Label(r"\bar{\mathrm{s}}", offsetx=3))
    Propagator(v_vts, v_sright, typ="line", fliparrow=True).draw()

    v_dleft = Vertex(15, 20, label=Label("#rm{d}", offsetx=-3))
    v_dright = Vertex(85, 20, label=Label("#rm{d}", offsetx=3))
    Propagator(v_dleft, v_dright, typ="line").draw()

    Propagator(
        v_vtb,
        v_vts,
        typ="arc(0,180)",
        label=Label(r"\bar{\mathrm{t}}", offsetx=-6, offsety=16),
    ).draw()
    Propagator(
        v_vtb,
        v_vts,
        typ="wavyarc(180,0)",
        label=Label("#rm{W}^{+}", offsetx=2, offsety=-7),
    ).draw()

    v_phitt = Vertex(55, 52)
    v_phimumu = Vertex(70, 70)
    Propagator(
        v_phitt,
        v_phimumu,
        typ="dashedline",
        noarrow=True,
        label=Label("#phi", offsetx=-4, offsety=2),
    ).draw()

    v_phimu1 = Vertex(85, 60, label=Label("#mu^{-}", offsetx=5))
    v_phimu2 = Vertex(85, 80, label=Label("#mu^{+}", offsetx=5))
    Propagator(v_phimumu, v_phimu1, fliparrow=True).draw()
    Propagator(v_phimumu, v_phimu2, fliparrow=True).draw()

    Label("#rm{B^{0}}", 5, 30).draw()
    Label("#rm{K^{*0}}", 94, 30).draw()

    save_diagram("feynmandiagram_Bphi.pdf")
    os.system("ic feynmandiagram_Bphi.pdf")


def diag5():
    init_diagram()
    v1 = Vertex(20, 60, Label("#rm{g}", offsetx=-2))
    v2 = Vertex(20, 30, Label("#rm{g}", offsetx=-2))
    v3 = Vertex(45, 60)
    v4 = Vertex(45, 30)

    vtth1 = Vertex(45, 45, Label("#rm{H}", offsety=5, offsetx=5))
    vtth2 = Vertex(57, 45)

    v7 = Vertex(70, 70, label=Label("#rm{t}", offsetx=2))
    v8 = Vertex(70, 20, label=Label("#rm{#bar{t}}", offsetx=2))
    v9 = Vertex(70, 53, label=Label("#rm{#bar{t}}", offsetx=2))
    v10 = Vertex(70, 37, label=Label("#rm{t}", offsetx=2))

    color = ROOT.kAzure - 6
    Propagator(v1, v3, typ="curlyline").draw()
    Propagator(v2, v4, typ="curlyline").draw()
    Propagator(v3, vtth1, typ="line", fliparrow=True, linecolor=color).draw()
    Propagator(v4, vtth1, typ="line", linecolor=color).draw()

    Propagator(vtth1, vtth2, typ="dashedline").draw()

    Propagator(v3, v7, typ="line", linecolor=color).draw()
    Propagator(v4, v8, typ="line", fliparrow=True, linecolor=color).draw()
    Propagator(vtth2, v9, typ="line", fliparrow=True, linecolor=color).draw()
    Propagator(vtth2, v10, typ="line", linecolor=color).draw()

    save_diagram("feynmandiagram_tttt.pdf")
    os.system("ic feynmandiagram_tttt.pdf")


def diag6():
    import pyfeyn as pf

    pf.init_diagram()
    pf.draw_grid()

    v_z = pf.Vertex(20, 50, label=pf.Label("Z", offsetx=-3))
    v_zqq = pf.Vertex(50, 50)
    v_q1 = pf.Vertex(70, 70, label=pf.Label(r"\mathrm{q}", offsetx=3))
    v_q2 = pf.Vertex(70, 30, label=pf.Label(r"\bar{\mathrm{q}}", offsetx=3))

    pf.Propagator(v_z, v_zqq, typ="wavyline").draw()
    pf.Propagator(v_zqq, v_q1, typ="line").draw()
    pf.Propagator(v_zqq, v_q2, typ="line", fliparrow=True).draw()

    pf.save_diagram("feynmandiagram_zqq.pdf")
    os.system("ic feynmandiagram_zqq.pdf")


if __name__ == "__main__":

    diag1()
    diag2()
    diag3()
    diag4()
    diag5()
    diag6()
