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
    <TR><TD>comp<TD>compressor</TR>
    <TR><TD>damp<TD>damper</TR>
    <TR><TD>desr<TD>desorber</TR>
    <TR><TD>ehr<TD>electric heater</TR>
    <TR><TD>ejr<TD>ejector/injector</TR>
    <TR><TD>fan<TD>fan</TR>
    <TR><TD>filt<TD>filter</TR>
    <TR><TD>hx<TD>heat exchanger</TR>
    <TR><TD>mflr<TD>muffler</TR>
    <TR><TD>noz<TD>nozzle box</TR>
    <TR><TD>pump<TD>pump</TR>
    <TR><TD>rect<TD>rectifier</TR>
    <TR><TD>recv<TD>receiver</TR>
    <TR><TD>sep<TD>separator</TR>
    <TR><TD>valv<TD>valve</TR>
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
    <TR><TH>Identifier</TH><TH>Description</TH></TR>
<TBODY>
    <TR><TD>crct<TD>circuit</TR>
    <TR><TD>ctrl<TD>controller</TR>
    <TR><TD>exh<TD>exhaust</TR>
    <TR><TD>gasl<TD>gas line</TR>
    <TR><TD>in<TD>inlet</TR>
    <TR><TD>idr<TD>indoor</TR>
    <TR><TD>lvl<TD>level</TR>
    <TR><TD>liql<TD>liquid line</TR>
    <TR><TD>mix<TD>mixed</TR>
    <TR><TD>odr<TD>outdoor</TR>
    <TR><TD>out<TD>outlet</TR>
    <TR><TD>phas<TD>phase</TR>
    <TR><TD>plnm<TD>plenum</TR>
    <TR><TD>ret<TD>return</TR>
    <TR><TD>sply<TD>supply</TR>
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
    <TR><TD>freq<TD>frequency</TR>
    <TR><TD>I<TD>current</TR>
    <TR><TD>T<TD>temperature</TR>
    <TR><TD>mdot<TD>mass flow rate</TR>
    <TR><TD>pa<TD>absolute pressure</TR>
    <TR><TD>pag<TD>absolute pressure, based on gage pressure measurement</TR>
    <TR><TD>pg<TD>gage pressure</TR>
    <TR><TD>pos<TD>position</TR>
    <TR><TD>pwr<TD>power</TR>
    <TR><TD>RH<TD>relative humidity</TR>
    <TR><TD>spd<TD>rotational speed</TR>
    <TR><TD>u<TD>flow velocity</TR>
    <TR><TD>V<TD>voltage</TR>
    <TR><TD>Vdot<TD>volumetric flow rate</TR>
</TABLE>
