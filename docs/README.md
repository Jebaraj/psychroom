# Measurement Data Output Standard

This is the Herrick Laboratory psychrometric chamber experimental data standard.
The guidelines described here should be followed to the best of the
experimenter's ability when testing HVAC equipment in the psychrometric
chambers.

## Standard Measurement Labeling Convention

The goal of the measurement label is to describe the phsyical quantities
recorded during the experiment. The aim of the label is to record
_meta-information_ about the measurement. In other words, storing the:

* who,
* what,
* where,
* and how

of the measurement.  This is accomplished using a standard labeling convention
by the standards committee.  The standard labeling convention is described
below and its parts are described in individual sections henceforth.

    {COMPONENT}{#?}_{FLUID}{#?}_{LOCATION}{#?}_{TYPE}

The label stores information about the component, fluid, location, and type of
measurement being recorded.  Additionally, an optional numeric identifier can be
assigned to distiguish between multiple occurances of components or locations.
For example in a dual compressor systems, the compressors could be identified as
compressor 0 and compressor 1.

### Component Label Identifier

The component label identifier is used to describe which component in the
overall system the measurement is taken.  A list of acceptable component
identifiers is shown below.

<TABLE>
<CAPTION><EM>Acceptable component identifiers and descriptions.</EM></CAPTION>
<COLGROUP align="center">
<COLGROUP align="left">
<THEAD valign="top">
    <TR><TH>Identifier</TH><TH>Description</TH></TR>
<TBODY>
    <TR><TD>absr<TD>absorber</TR>
    <TR><TD>accm<TD>accumulator</TR>
    <TR><TD>ahu<TD>air handling unit</TR>
    <TR><TD>amb<TD>ambient</TR>
    <TR><TD>comp<TD>compressor</TR>
    <TR><TD>damp<TD>damper</TR>
    <TR><TD>desr<TD>desorber</TR>
    <TR><TD>ehr<TD>electric heater</TR>
    <TR><TD>ejr<TD>ejector/injector</TR>
    <TR><TD>fan<TD>fan</TR>
    <TR><TD>filt<TD>filter</TR>
    <TR><TD>idhx<TD>indoor heat exchanger</TR>
    <TR><TD>ithx<TD>internal heat exchanger</TR>
    <TR><TD>mflr<TD>muffler</TR>
    <TR><TD>noz<TD>nozzle box</TR>
    <TR><TD>odhx<TD>outdoor heat exchanger</TR>
    <TR><TD>pump<TD>pump</TR>
    <TR><TD>rect<TD>rectifier</TR>
    <TR><TD>recv<TD>receiver</TR>
    <TR><TD>sep<TD>separator</TR>
    <TR><TD>od<TD>outdoor</TR>
    <TR><TD>valv<TD>valve</TR>
    <TR><TD>rvalv<TD>reversing valve</TR>
    <TR><TD>vsd<TD>variable speed/frequency drive</TR>
    <TR><TD>xd<TD>expansion device</TR>
</TABLE>


### Fluid Label Identifier

The fluid label identifier is used to describe the "fluid" being measured by the
measurement device.  A list of acceptable fluid identifiers is shown below.

<TABLE>
<CAPTION><EM>Acceptable fluid identifiers and descriptions.</EM></CAPTION>
<COLGROUP align="center">
<COLGROUP align="left">
<THEAD valign="top">
    <TR><TH>Identifier</TH><TH>Description</TH></TR>
<TBODY>
    <TR><TD>air<TD>air</TR>
    <TR><TD>elec<TD>electric</TR>
    <TR><TD>gas<TD>natural gas</TR>
    <TR><TD>brn<TD>brine</TR>
    <TR><TD>h2o<TD>water</TR>
    <TR><TD>oil<TD>oil</TR>
    <TR><TD>ref<TD>refrigerant</TR>
    <TR><TD>rich<TD>rich solution</TR>
    <TR><TD>weak<TD>weak solution</TR>
</TABLE>

### Location Label Identifier

The location label identifier is used to describe where on the component the
measurement is taken.  A list of acceptable location identifiers is shown below.

<TABLE>
<CAPTION><EM>Acceptable location identifiers and descriptions.</EM></CAPTION>
<COLGROUP align="center">
<COLGROUP align="left">
<THEAD valign="top">
    <TR><TH>Identifier</TH><TH>Description</TH><TH>Explanation</TH><TH>Example</TH></TR>
<TBODY>
    <TR><TD>srnd<TD>surroundings<TD>Surroundings of the psychrometric chamber<TD> noz_air_srndInt_DeltaP is the air pressure difference between the atmosphere and the interior of the nozzle box</TR>
    <TR><TD>crct<TD>circuit<TD>Anywhere between the main inlet and outlet of heat exchangers<TD> odhx_ref_crct1_T is the temperature at a location marked as #1  within the refrigerant circuit of the outdoor heat exchanger</TR>
    <TR><TD>ctrl<TD>controller<TD>Controller of a copmonent<TD> fan_elec_ctrl_pwr is the power consumption of the fan controller<TD></TR>
    <TR><TD>exh<TD>exhaust<TD>Exhaust from a component<TD> ahu_air_exh_T is the temperature at the exhaust of the air handling unit</TR>
    <TR><TD>gasl<TD>gas line<TD>Gas line along the refrigerant circuit of a component<TD> odhx_ref_gasl_pg is the gag pressure at the gas line of the outdoor heat exchanger</TR>
    <TR><TD>in<TD>inlet<TD>Inlet of a component<TD> ithx_brn_in_T is the inlet brine temperature of an internal heat exchanger</TR>
    <TR><TD>int<TD>internal, interior<TD>Internal part of a component<TD> comp_ref_int1_pg is the gage pressure of the internal location #1 inside the compressor</TR>
    <TR><TD>idr<TD>indoor<TD>A location in the indoor room around a component<TD> ahu_air_indr_B is the indoor room wet-bulb temperature around the air handling unit</TR>
    <TR><TD>lvl<TD>level<TD><TD></TR>
    <TR><TD>liql<TD>liquid line<TD>Liquid line along the refrigerant circuit of a component<TD> odhx_ref_liql_pg is the gage pressure at the liquid line of the outdoor heat exchanger</TR>
    <TR><TD>mix<TD>mixed<TD>Mixing chamber inside a component<TD> ahu_air_mix_D is the dewpoint at the mixing chamber inside the air handling unit</TR>
    <TR><TD>odr<TD>outdoor<TD>A location around the outdoor room at a component<TD> comp_air_odr_T is the temperature around the compressor in the outdoor room</TR>
    <TR><TD>out<TD>outlet<TD>Outlet of a component<TD>xd2_ref_out_pg is the gage pressure at the refrigerant outlet of expansion valve #2</TR>
    <TR><TD>phas<TD>phase<TD>Phase of power supply to a component<TD>comp_elec_phas2_I is the current at the second phase of the electrical power supply to the compressor</TR>
    <TR><TD>plnm<TD>plenum<TD>Plenum of a component<TD>idhx_air_plenum_D is the dewpoint at the plenum of the indoor unit heat exchanger</TR>
    <TR><TD>ret<TD>return<TD>Return air duct of a component<TD>ahu_air_ret_B is the air wet-bulb temperature at the return air pipe of the air handling unit</TR>
    <TR><TD>sply<TD>supply<TD>Supply air duct of a component<TD>ahu_air_sply_RH is the air reliative humidity at the supply air pipe of the air handling unit</TR></TR>
</TABLE>

### Measurement Type Label Identifier

The measurement type label identifier is used to describe the actual type of
measurement being recorded.  A list of acceptable measurement types is shown
below.

<TABLE>
<CAPTION><EM>Acceptable measurement type identifiers and
             descriptions.</EM></CAPTION>
<COLGROUP align="center">
<COLGROUP align="left">
<THEAD valign="top">
    <TR><TH>Identifier</TH><TH>Description</TH></TR>
<TBODY>
    <TR><TD>B<TD>wet bulb</TR>
    <TR><TD>D<TD>dew point</TR>
    <TR><TD>duty<TD>PWM duty cycle</TR>
    <TR><TD>freq<TD>frequency</TR>
    <TR><TD>I<TD>current</TR>
    <TR><TD>T<TD>temperature</TR>
    <TR><TD>mdot<TD>mass flow rate</TR>
    <TR><TD>pa<TD>absolute pressure</TR>
    <TR><TD>pag<TD>absolute pressure, based on gage pressure measurement</TR>
    <TR><TD>pd<TD>pressure difference between two points</TR>
    <TR><TD>pg<TD>gage pressure</TR>
    <TR><TD>pos<TD>position</TR>
    <TR><TD>pwr<TD>power</TR>
    <TR><TD>RH<TD>relative humidity</TR>
    <TR><TD>spd<TD>rotational speed</TR>
    <TR><TD>sw<TD>switch</TR>
    <TR><TD>u<TD>flow velocity</TR>
    <TR><TD>V<TD>voltage</TR>
    <TR><TD>Vdot<TD>volumetric flow rate</TR>
</TABLE>

### Differential Measurements

Differential measurements are handled in a similar way to normal single point measurements.

However, each part of the namestring can now be composed of two parts - the distinction between 
first and second part is made by using a capital letter. Before the type, add "Delta" to specify
that a difference measurement is used. Naming scheme:

    {component1}{Componen2?}{#?}_{fluid1}{Fluid2?}{#?}_{location1}{Location2}{#?}_Delta{type1}{Type2?}

#### Examples:
Difference between compressor refrigerant inlet temperature and indoor heat exchanger (evaporator) refrigerant 
outlet temperature:

    idhxComp_ref_outIn_DeltaT
 
 Difference between air inlet temperature of evaporator and refrigerant inlet temperature:
    
    idhx_airRef_inIn_DeltaT



## Measurement Data Output File Format

### File Header Information

What do we put in the header?
