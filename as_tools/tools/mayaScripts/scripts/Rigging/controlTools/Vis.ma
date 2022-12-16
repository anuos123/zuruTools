//Maya ASCII 2023 scene
//Name: Vis.ma
//Last modified: Tue, Dec 13, 2022 02:25:43 PM
//Codeset: 1252
requires maya "2023";
requires "stereoCamera" "10.0";
requires "mtoa" "5.1.0";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t ntsc;
fileInfo "application" "maya";
fileInfo "product" "Maya 2023";
fileInfo "version" "2023";
fileInfo "cutIdentifier" "202202161415-df43006fd3";
fileInfo "osv" "Windows 10 Pro v2009 (Build: 19045)";
fileInfo "UUID" "4FBD6D6D-47BB-8150-7612-22B39B79A636";
createNode transform -n "Visibility_zero";
	rename -uid "5BFD4324-4392-9F78-2CEE-C18CD1A91C20";
	setAttr ".t" -type "double3" -2.3628422065540192e-14 76.680183757226331 -1.2315651597996493 ;
	setAttr ".r" -type "double3" 0 179.99999999999997 -2.5444437451708134e-14 ;
	setAttr ".rp" -type "double3" 1.776356839400252e-16 -8.8817841970012602e-17 0 ;
	setAttr ".sp" -type "double3" 1.7763568394002505e-15 -8.8817841970012523e-16 0 ;
	setAttr ".spt" -type "double3" -1.5987211554602255e-15 7.9936057773011273e-16 0 ;
createNode transform -n "Visibility" -p "Visibility_zero";
	rename -uid "3BB76F10-41E9-8122-0670-DD9FC1314FB5";
	addAttr -ci true -sn "_" -ln "_" -min 0 -max 0 -en "FK_IK" -at "enum";
	addAttr -ci true -sn "L_Arm_fk_vis" -ln "L_Arm_fk_vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "L_Arm_ik_vis" -ln "L_Arm_ik_vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "L_Leg_fk_vis" -ln "L_Leg_fk_vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "L_Leg_ik_vis" -ln "L_Leg_ik_vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "R_Arm_fk_vis" -ln "R_Arm_fk_vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "R_Arm_ik_vis" -ln "R_Arm_ik_vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "R_Leg_fk_vis" -ln "R_Leg_fk_vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "R_Leg_ik_vis" -ln "R_Leg_ik_vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "__" -ln "__" -min 0 -max 0 -en "limbs" -at "enum";
	addAttr -ci true -sn "head_vis" -ln "head_vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "body_vis" -ln "body_vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "L_Arm_vis" -ln "L_Arm_vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "R_Arm_vis" -ln "R_Arm_vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "L_Leg_vis" -ln "L_Leg_vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "R_Leg_vis" -ln "R_Leg_vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "Ribbon_vis" -ln "Ribbon_vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "sec_Ctrl_Vis" -ln "sec_Ctrl_Vis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "___" -ln "___" -min 0 -max 0 -en "Display" -at "enum";
	addAttr -ci true -sn "displayMode" -ln "displayMode" -min 0 -max 4 -en "Hi:Mid:Low:Hide:All" 
		-at "enum";
	addAttr -ci true -sn "displayType" -ln "displayType" -min 0 -max 2 -en "Normal:Template:Reference" 
		-at "enum";
	addAttr -ci true -sn "FacialPanel" -ln "FacialPanel" -min 0 -max 1 -at "bool";
	addAttr -ci true -k true -sn "clothVis" -ln "clothVis" -min 0 -max 1 -at "bool";
	addAttr -ci true -k true -sn "hairVis" -ln "hairVis" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "Face_Frist" -ln "Face_Frist" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "Face_second" -ln "Face_second" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".rp" -type "double3" 1.7763568394002505e-15 -8.8817841970012523e-16 0 ;
	setAttr ".sp" -type "double3" 1.7763568394002505e-15 -8.8817841970012523e-16 0 ;
	setAttr -l on -cb on "._";
	setAttr -cb on ".L_Arm_fk_vis";
	setAttr -cb on ".L_Arm_ik_vis";
	setAttr -cb on ".L_Leg_fk_vis";
	setAttr -cb on ".L_Leg_ik_vis";
	setAttr -cb on ".R_Arm_fk_vis";
	setAttr -cb on ".R_Arm_ik_vis";
	setAttr -cb on ".R_Leg_fk_vis";
	setAttr -cb on ".R_Leg_ik_vis";
	setAttr -l on -cb on ".__";
	setAttr -cb on ".head_vis" yes;
	setAttr -cb on ".body_vis" yes;
	setAttr -cb on ".L_Arm_vis" yes;
	setAttr -cb on ".R_Arm_vis" yes;
	setAttr -cb on ".L_Leg_vis" yes;
	setAttr -cb on ".R_Leg_vis" yes;
	setAttr -cb on ".Ribbon_vis" yes;
	setAttr -cb on ".sec_Ctrl_Vis" yes;
	setAttr -l on -cb on ".___";
	setAttr -cb on ".displayMode";
	setAttr -cb on ".displayType" 2;
	setAttr -cb on ".FacialPanel" yes;
	setAttr -k on ".clothVis";
	setAttr -k on ".hairVis";
	setAttr -k on ".Face_Frist";
	setAttr -k on ".Face_second";
createNode nurbsCurve -n "VisibilityShape" -p "Visibility";
	rename -uid "0503CC1B-4519-86B1-3EEF-619A3C15DEF1";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 21;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-42.027979960643002 25.471501804999541 -1.9167427084988687e-15
		-42.027979960643002 -25.471501805000479 -1.9167427084988687e-15
		42.027979960643037 -25.471501805000479 -1.9167427084988687e-15
		42.027979960643037 25.471501804999541 -1.9167427084988687e-15
		-42.027979960643002 25.471501804999541 -1.9167427084988687e-15
		;
createNode nurbsCurve -n "VisibilityShape1" -p "Visibility";
	rename -uid "89E7A1B6-43F8-4FC7-ABB5-E388D7FD8760";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		2 39 0 no 3
		42 0 0 1.3376607919432364 1.3376607919432364 1.5251636530098414 1.5251636530098414
		 2.5251636530098414 3.5251636530098414 3.5251636530098414 4.5251636530098409 5.5251636530098409
		 5.5251636530098409 5.5370046540016773 5.5370046540016773 6.5370046540016773 7.5370046540016773
		 7.5370046540016773 8.5370046540016773 9.5370046540016773 9.5370046540016773 9.7245075150682823
		 9.7245075150682823 11.30867780575265 11.30867780575265 11.496180666819255 11.496180666819255
		 12.496180666819255 13.496180666819255 13.496180666819255 14.496180666819255 15.496180666819255
		 15.496180666819255 15.750759136339358 15.750759136339358 16.750759136339358 17.750759136339358
		 17.750759136339358 18.750759136339358 19.750759136339358 19.750759136339358 19.938261997405963
		 19.938261997405963
		41
		-3.8530084720866005 16.415003043696899 -1.9167427084988687e-15
		-9.5012843752778995 16.415003043696899 -1.9167427084988687e-15
		-15.149560278469197 16.415003043696899 -1.9167427084988687e-15
		-15.149560278469197 15.623271763000984 -1.9167427084988687e-15
		-15.149560278469197 14.831540482305062 -1.9167427084988687e-15
		-12.113714104045531 14.544164191764706 -1.9167427084988687e-15
		-11.04606241022687 12.882714037424099 -1.9167427084988687e-15
		-11.899699242232407 10.5729179207519 -1.9167427084988687e-15
		-13.0355965230069 7.0953568238071627 -1.9167427084988687e-15
		-16.901059556987896 -2.9455328820941222 -1.9167427084988687e-15
		-19.049390944703067 -8.3333132149848357 -1.9167427084988687e-15
		-19.09938959979911 -8.3333132149848357 -1.9167427084988687e-15
		-19.149388254895136 -8.3333132149848357 -1.9167427084988687e-15
		-21.185248441146861 -3.3297106925008189 -1.9167427084988687e-15
		-25.87567639796109 8.4958732753025199 -1.9167427084988687e-15
		-27.04905978380625 11.699459783072838 -1.9167427084988687e-15
		-27.751334707884482 13.263837806269516 -1.9167427084988687e-15
		-26.819001539107958 14.518133964111609 -1.9167427084988687e-15
		-24.149176446990364 14.831540482305062 -1.9167427084988687e-15
		-24.149176446990364 15.623271763000984 -1.9167427084988687e-15
		-24.149176446990364 16.415003043696885 -1.9167427084988687e-15
		-30.838339300022369 16.415003043696899 -1.9167427084988687e-15
		-37.527502153054407 16.415003043696899 -1.9167427084988687e-15
		-37.527502153054407 15.623271763000984 -1.9167427084988687e-15
		-37.527502153054407 14.831540482305062 -1.9167427084988687e-15
		-35.454181634234573 14.703348054239241 -1.9167427084988687e-15
		-33.414223620065187 12.91946562616995 -1.9167427084988687e-15
		-32.42037148751843 10.181085677065045 -1.9167427084988687e-15
		-30.555769581221938 5.3871811222041526 -1.9167427084988687e-15
		-24.912880131079628 -9.3435180004483058 -1.9167427084988687e-15
		-22.199267556999104 -16.415003043697872 -1.9167427084988687e-15
		-21.124309358685739 -16.415003043697872 -1.9167427084988687e-15
		-20.049351160372382 -16.415003043697872 -1.9167427084988687e-15
		-16.943803252594478 -8.393002331068546 -1.9167427084988687e-15
		-10.901324035474655 6.3101459862758427 -1.9167427084988687e-15
		-9.6825939312575837 9.2994470209554674 -1.9167427084988687e-15
		-8.3988655754156643 12.634769675902779 -1.9167427084988687e-15
		-6.1087338782477154 14.694160157052794 -1.9167427084988687e-15
		-3.8530084720866005 14.831540482305062 -1.9167427084988687e-15
		-3.8530084720866005 15.623271763000984 -1.9167427084988687e-15
		-3.8530084720866005 16.415003043696885 -1.9167427084988687e-15
		;
createNode nurbsCurve -n "VisibilityShape2" -p "Visibility";
	rename -uid "718C0483-4676-D0BD-B245-9EA53E65C30F";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		2 27 0 no 3
		30 0 0 0.1824231326771954 0.1824231326771954 1.1824231326771955 2.1824231326771955
		 2.1824231326771955 4.4549996185244529 4.4549996185244529 5.4549996185244529 6.4549996185244529
		 6.4549996185244529 6.6425024795910579 6.6425024795910579 8.2390249485008002 8.2390249485008002
		 8.4265278095674052 8.4265278095674052 9.4265278095674052 10.426527809567405 10.426527809567405
		 12.699104295414664 12.699104295414664 13.699104295414664 14.699104295414664 14.699104295414664
		 14.881527428091859 14.881527428091859 16.4780498970016 16.4780498970016
		29
		13.051008479577751 -15.549046955436713 -1.9167427084988687e-15
		13.051008479577751 -14.778764840051974 -1.9167427084988687e-15
		13.051008479577751 -14.008482724667219 -1.9167427084988687e-15
		10.290348201951945 -13.841889267687463 -1.9167427084988687e-15
		8.7226970709216634 -12.163815849152568 -1.9167427084988687e-15
		8.8144858390270855 -9.1620409232015554 -1.9167427084988687e-15
		8.8144858390270855 0.43391874047596934 -1.9167427084988687e-15
		8.8144858390270855 10.029878404153484 -1.9167427084988687e-15
		8.7227099571729827 13.069397160201472 -1.9167427084988687e-15
		10.290335315700634 14.733501882312625 -1.9167427084988687e-15
		13.05100847957776 14.831540482305062 -1.9167427084988687e-15
		13.051008479577751 15.623271763000984 -1.9167427084988687e-15
		13.051008479577751 16.415003043696885 -1.9167427084988687e-15
		6.3096885243547112 16.415003043696899 -1.9167427084988687e-15
		-0.431631430868329 16.415003043696899 -1.9167427084988687e-15
		-0.431631430868329 15.623271763000984 -1.9167427084988687e-15
		-0.431631430868329 14.831540482305062 -1.9167427084988687e-15
		2.3636284315339702 14.733501882312625 -1.9167427084988687e-15
		3.9462920453443791 13.069397160201472 -1.9167427084988687e-15
		3.8530213583379136 10.029878404153484 -1.9167427084988687e-15
		3.8530213583379136 0.43391874047596934 -1.9167427084988687e-15
		3.8530213583379136 -9.1620409232015554 -1.9167427084988687e-15
		3.94630493159569 -12.163802962901245 -1.9167427084988687e-15
		2.3636155452826553 -13.841889267687463 -1.9167427084988687e-15
		-0.431631430868329 -14.008482724667219 -1.9167427084988687e-15
		-0.431631430868329 -14.778764840051974 -1.9167427084988687e-15
		-0.431631430868329 -15.549046955436713 -1.9167427084988687e-15
		6.3096885243547112 -15.549046955436713 -1.9167427084988687e-15
		13.05100847957776 -15.549046955436713 -1.9167427084988687e-15
		;
createNode nurbsCurve -n "VisibilityShape3" -p "Visibility";
	rename -uid "8F55C559-4C94-5716-F140-3D99F5BD9114";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		2 45 0 no 3
		48 0 0 1 1 2 3 3 4 5 5 6 7 7 8 9 9 10 11 11 12 13 13 13.196656098461839 13.196656098461839
		 14.196656098461839 15.196656098461839 15.196656098461839 16.196656098461837 16.196656098461837
		 17.196656098461837 17.196656098461837 18.196656098461837 19.196656098461837 19.196656098461837
		 20.196656098461837 21.196656098461837 21.196656098461837 22.196656098461837 23.196656098461837
		 23.196656098461837 24.196656098461837 25.196656098461837 25.196656098461837 26.196656098461837
		 27.196656098461837 27.196656098461837 27.378797104964132 27.378797104964132
		47
		36.129034615517895 8.5407432023758112 -1.9167427084988687e-15
		35.587824946605956 13.002169587099417 -1.9167427084988687e-15
		35.317213669024348 15.570502563872544 -1.9167427084988687e-15
		34.383037766310004 15.751206466040502 -1.9167427084988687e-15
		30.901314410191027 16.380506548930899 -1.9167427084988687e-15
		28.604198364811236 16.415003043696899 -1.9167427084988687e-15
		23.247087310046453 16.338600459659684 -1.9167427084988687e-15
		17.44850617153552 11.386001719874141 -1.9167427084988687e-15
		17.414563785575996 7.4265334825618039 -1.9167427084988687e-15
		17.528903493479902 3.7188754821648216 -1.9167427084988687e-15
		22.523678933814214 -0.79323252897441832 -1.9167427084988687e-15
		26.032141261408523 -2.3960502398390013 -1.9167427084988687e-15
		29.073670272661399 -3.7992856903614807 -1.9167427084988687e-15
		32.533822044081724 -6.9686334283920806 -1.9167427084988687e-15
		32.566037672365255 -9.3154130863337627 -1.9167427084988687e-15
		32.5418630649013 -11.851195392289236 -1.9167427084988687e-15
		29.541441195338166 -14.799788759069797 -1.9167427084988687e-15
		26.855199019047333 -14.831540482306035 -1.9167427084988687e-15
		22.97634716995168 -14.59262938295541 -1.9167427084988687e-15
		18.762401241702126 -8.9252689415689588 -1.9167427084988687e-15
		18.136709309179498 -6.3637914504945376 -1.9167427084988687e-15
		17.342355676341302 -6.6057308189038126 -1.9167427084988687e-15
		16.548002043503107 -6.8476701873130947 -1.9167427084988687e-15
		16.784207030077912 -9.0258203605675007 -1.9167427084988687e-15
		17.599597468185252 -13.953973881611505 -1.9167427084988687e-15
		17.94413716955189 -14.953238239709888 -1.9167427084988687e-15
		18.702377083084247 -15.288216342601983 -1.9167427084988687e-15
		20.688251500491258 -15.805921489118237 -1.9167427084988687e-15
		22.727539429592365 -16.384527059341661 -1.9167427084988687e-15
		25.826373600435982 -16.414990157446571 -1.9167427084988687e-15
		31.394973811756472 -16.33870354967118 -1.9167427084988687e-15
		37.487206845197385 -11.16992505785187 -1.9167427084988687e-15
		37.527502153054414 -6.9928338083586565 -1.9167427084988687e-15
		37.44411522080533 -3.2171106285242401 -1.9167427084988687e-15
		32.662259310922458 1.3403569872382015 -1.9167427084988687e-15
		28.964291771513192 2.9749135350877136 -1.9167427084988687e-15
		25.609369128318146 4.4779530020325602 -1.9167427084988687e-15
		22.27532221225087 7.5202938471181842 -1.9167427084988687e-15
		22.276945879916351 9.7491127605369066 -1.9167427084988687e-15
		22.297847379546713 11.876761714894061 -1.9167427084988687e-15
		25.175308639077254 14.772482792535687 -1.9167427084988687e-15
		27.781140607172411 14.831540482305062 -1.9167427084988687e-15
		30.998979308895368 14.704430499349575 -1.9167427084988687e-15
		34.059554199589456 10.602066621222839 -1.9167427084988687e-15
		34.640698361321647 8.1523387015383193 -1.9167427084988687e-15
		35.384866488419739 8.3465409519570759 -1.9167427084988687e-15
		36.129034615517895 8.5407432023758272 -1.9167427084988687e-15
		;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -k on ".fzn";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 0;
	setAttr -av -k on ".unw";
	setAttr -av -k on ".etw";
	setAttr -av -k on ".tps";
	setAttr -av -k on ".tms";
select -ne :hardwareRenderingGlobals;
	setAttr -av -k on ".cch";
	setAttr -k on ".fzn";
	setAttr -av -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".rm";
	setAttr -k on ".lm";
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr -k on ".hom";
	setAttr -k on ".hodm";
	setAttr -k on ".xry";
	setAttr -k on ".jxr";
	setAttr -k on ".sslt";
	setAttr -k on ".cbr";
	setAttr -k on ".bbr";
	setAttr -av -k on ".mhl";
	setAttr -k on ".cons";
	setAttr -k on ".vac";
	setAttr -av -k on ".hwi";
	setAttr -k on ".csvd";
	setAttr -av -k on ".ta";
	setAttr -av -k on ".tq";
	setAttr -k on ".ts";
	setAttr -av -k on ".etmr";
	setAttr -av -k on ".tmr";
	setAttr -av -k on ".aoon";
	setAttr -av -k on ".aoam";
	setAttr -av -k on ".aora";
	setAttr -k on ".aofr";
	setAttr -av -k on ".aosm";
	setAttr -av -k on ".hff";
	setAttr -av -k on ".hfd";
	setAttr -av -k on ".hfs";
	setAttr -av -k on ".hfe";
	setAttr -av ".hfc";
	setAttr -av -k on ".hfcr";
	setAttr -av -k on ".hfcg";
	setAttr -av -k on ".hfcb";
	setAttr -av -k on ".hfa";
	setAttr -av -k on ".mbe";
	setAttr -k on ".mbt";
	setAttr -av -k on ".mbsof";
	setAttr -k on ".mbsc";
	setAttr -k on ".mbc";
	setAttr -k on ".mbfa";
	setAttr -k on ".mbftb";
	setAttr -k on ".mbftg";
	setAttr -k on ".mbftr";
	setAttr -k on ".mbfta";
	setAttr -k on ".mbfe";
	setAttr -k on ".mbme";
	setAttr -k on ".mbcsx";
	setAttr -k on ".mbcsy";
	setAttr -k on ".mbasx";
	setAttr -k on ".mbasy";
	setAttr -av -k on ".blen";
	setAttr -k on ".blth";
	setAttr -k on ".blfr";
	setAttr -k on ".blfa";
	setAttr -av -k on ".blat";
	setAttr -av -k on ".msaa" yes;
	setAttr -av -k on ".aasc";
	setAttr -k on ".aasq";
	setAttr -k on ".laa";
	setAttr -k on ".fprt" yes;
	setAttr -k on ".rtfm";
select -ne :renderPartition;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 118 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 123 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 66 ".u";
select -ne :defaultRenderingList1;
	setAttr -k on ".ihi";
select -ne :defaultTextureList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 34 ".tx";
select -ne :initialShadingGroup;
	setAttr -av -k on ".cch";
	setAttr -k on ".fzn";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".bbx";
	setAttr -k on ".vwm";
	setAttr -k on ".tpv";
	setAttr -k on ".uit";
	setAttr -s 4 ".dsm";
	setAttr -k on ".mwc";
	setAttr -av -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
	setAttr -s 1536 ".gn";
	setAttr -cb on ".ai_override";
	setAttr -cb on ".ai_surface_shader";
	setAttr -cb on ".ai_surface_shaderr";
	setAttr -cb on ".ai_surface_shaderg";
	setAttr -cb on ".ai_surface_shaderb";
	setAttr -cb on ".ai_volume_shader";
	setAttr -cb on ".ai_volume_shaderr";
	setAttr -cb on ".ai_volume_shaderg";
	setAttr -cb on ".ai_volume_shaderb";
select -ne :initialParticleSE;
	setAttr -av -k on ".cch";
	setAttr -k on ".fzn";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".bbx";
	setAttr -k on ".vwm";
	setAttr -k on ".tpv";
	setAttr -k on ".uit";
	setAttr -k on ".mwc";
	setAttr -av -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
	setAttr -cb on ".ai_override";
	setAttr -k on ".ai_surface_shader";
	setAttr -cb on ".ai_surface_shaderr";
	setAttr -cb on ".ai_surface_shaderg";
	setAttr -cb on ".ai_surface_shaderb";
	setAttr -k on ".ai_volume_shader";
	setAttr -cb on ".ai_volume_shaderr";
	setAttr -cb on ".ai_volume_shaderg";
	setAttr -cb on ".ai_volume_shaderb";
lockNode -l 0 -lu 1;
select -ne :defaultRenderGlobals;
	addAttr -ci true -h true -sn "dss" -ln "defaultSurfaceShader" -dt "string";
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -av -k on ".macc";
	setAttr -av -k on ".macd";
	setAttr -av -k on ".macq";
	setAttr -av -k on ".mcfr";
	setAttr -cb on ".ifg";
	setAttr -av -k on ".clip";
	setAttr -av -k on ".edm";
	setAttr -av -k on ".edl";
	setAttr -av -cb on ".ren" -type "string" "arnold";
	setAttr -av -k on ".esr";
	setAttr -av -k on ".ors";
	setAttr -cb on ".sdf";
	setAttr -av -k on ".outf";
	setAttr -av -cb on ".imfkey";
	setAttr -av -k on ".gama";
	setAttr -av -k on ".exrc";
	setAttr -av -k on ".expt";
	setAttr -av -k on ".an";
	setAttr -cb on ".ar";
	setAttr -av -k on ".fs";
	setAttr -av -k on ".ef";
	setAttr -av -k on ".bfs";
	setAttr -av -cb on ".me";
	setAttr -cb on ".se";
	setAttr -av -k on ".be";
	setAttr -av -cb on ".ep";
	setAttr -av -k on ".fec";
	setAttr -av -k on ".ofc";
	setAttr -cb on ".ofe";
	setAttr -cb on ".efe";
	setAttr -cb on ".oft";
	setAttr -cb on ".umfn";
	setAttr -cb on ".ufe";
	setAttr -av -cb on ".pff";
	setAttr -av -cb on ".peie";
	setAttr -av -cb on ".ifp";
	setAttr -k on ".rv";
	setAttr -av -k on ".comp";
	setAttr -av -k on ".cth";
	setAttr -av -k on ".soll";
	setAttr -av -cb on ".sosl";
	setAttr -av -k on ".rd";
	setAttr -av -k on ".lp";
	setAttr -av -k on ".sp";
	setAttr -av -k on ".shs";
	setAttr -av -k on ".lpr";
	setAttr -cb on ".gv";
	setAttr -cb on ".sv";
	setAttr -av -k on ".mm";
	setAttr -av -k on ".npu";
	setAttr -av -k on ".itf";
	setAttr -av -k on ".shp";
	setAttr -cb on ".isp";
	setAttr -av -k on ".uf";
	setAttr -av -k on ".oi";
	setAttr -av -k on ".rut";
	setAttr -av -k on ".mot";
	setAttr -av -cb on ".mb";
	setAttr -av -k on ".mbf";
	setAttr -av -k on ".mbso";
	setAttr -av -k on ".mbsc";
	setAttr -av -k on ".afp";
	setAttr -av -k on ".pfb";
	setAttr -av -k on ".pram";
	setAttr -av -k on ".poam";
	setAttr -av -k on ".prlm";
	setAttr -av -k on ".polm";
	setAttr -av -cb on ".prm";
	setAttr -av -cb on ".pom";
	setAttr -cb on ".pfrm";
	setAttr -cb on ".pfom";
	setAttr -av -k on ".bll";
	setAttr -av -k on ".bls";
	setAttr -av -k on ".smv";
	setAttr -av -k on ".ubc";
	setAttr -av -k on ".mbc";
	setAttr -cb on ".mbt";
	setAttr -av -k on ".udbx";
	setAttr -av -k on ".smc";
	setAttr -av -k on ".kmv";
	setAttr -cb on ".isl";
	setAttr -cb on ".ism";
	setAttr -cb on ".imb";
	setAttr -av -k on ".rlen";
	setAttr -av -k on ".frts";
	setAttr -av -k on ".tlwd";
	setAttr -av -k on ".tlht";
	setAttr -av -k on ".jfc";
	setAttr -cb on ".rsb";
	setAttr -av -k on ".ope";
	setAttr -av -k on ".oppf";
	setAttr -av -k on ".rcp";
	setAttr -av -k on ".icp";
	setAttr -av -k on ".ocp";
	setAttr -cb on ".hbl";
	setAttr ".dss" -type "string" "lambert1";
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -av -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av -k on ".w";
	setAttr -av -k on ".h";
	setAttr -av -k on ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av -k on ".dar";
	setAttr -av -k on ".ldar";
	setAttr -av -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -av -k on ".isu";
	setAttr -av -k on ".pdu";
select -ne :defaultObjectSet;
	addAttr -ci true -sn "BodyArtCharName" -ln "BodyArtCharName" -dt "string";
	addAttr -ci true -sn "BodyArtGeoGrp" -ln "BodyArtGeoGrp" -dt "string";
	addAttr -ci true -sn "BodyArtGeoSuffix" -ln "BodyArtGeoSuffix" -dt "string";
	addAttr -ci true -sn "BodyArtGeoParent" -ln "BodyArtGeoParent" -dt "string";
	setAttr -k on ".BodyArtCharName" -type "string" "character";
	setAttr -k on ".BodyArtGeoGrp" -type "string" "Geo_grp";
	setAttr -k on ".BodyArtGeoSuffix" -type "string" "msh";
	setAttr -k on ".BodyArtGeoParent";
select -ne :defaultColorMgtGlobals;
	setAttr ".cfe" yes;
	setAttr ".cfp" -type "string" "<MAYA_RESOURCES>/OCIO-configs/Maya2022-default/config.ocio";
	setAttr ".vtn" -type "string" "ACES 1.0 SDR-video (sRGB)";
	setAttr ".vn" -type "string" "ACES 1.0 SDR-video";
	setAttr ".dn" -type "string" "sRGB";
	setAttr ".wsn" -type "string" "ACEScg";
	setAttr ".ovt" no;
	setAttr ".povt" no;
	setAttr ".otn" -type "string" "ACES 1.0 SDR-video (sRGB)";
	setAttr ".potn" -type "string" "ACES 1.0 SDR-video (sRGB)";
select -ne :hardwareRenderGlobals;
	setAttr -av -k on ".cch";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -av -k off -cb on ".ctrs" 256;
	setAttr -av -k off -cb on ".btrs" 512;
	setAttr -av -k off -cb on ".fbfm";
	setAttr -av -k off -cb on ".ehql";
	setAttr -av -k off -cb on ".eams";
	setAttr -av -k off -cb on ".eeaa";
	setAttr -av -k off -cb on ".engm";
	setAttr -av -k off -cb on ".mes";
	setAttr -av -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -av -k off -cb on ".mbs";
	setAttr -av -k off -cb on ".trm";
	setAttr -av -k off -cb on ".tshc";
	setAttr -av -k off -cb on ".enpt";
	setAttr -av -k off -cb on ".clmt";
	setAttr -av -k off -cb on ".tcov";
	setAttr -av -k off -cb on ".lith";
	setAttr -av -k off -cb on ".sobc";
	setAttr -av -k off -cb on ".cuth";
	setAttr -av -k off -cb on ".hgcd";
	setAttr -av -k off -cb on ".hgci";
	setAttr -av -k off -cb on ".mgcs";
	setAttr -av -k off -cb on ".twa";
	setAttr -av -k off -cb on ".twz";
	setAttr -av -cb on ".hwcc";
	setAttr -av -cb on ".hwdp";
	setAttr -av -cb on ".hwql";
	setAttr -av -k on ".hwfr";
	setAttr -av -k on ".soll";
	setAttr -av -k on ".sosl";
	setAttr -av -k on ".bswa";
	setAttr -av -k on ".shml";
	setAttr -av -k on ".hwel";
select -ne :ikSystem;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av -k on ".gsn";
	setAttr -k on ".gsv";
	setAttr -s 35 ".sol";
dataStructure -fmt "raw" -as "name=notes_pPlane3:string=value";
dataStructure -fmt "raw" -as "name=mapManager_grass_c_geo:string=value";
dataStructure -fmt "raw" -as "name=mapManager_pPlane6:string=value";
dataStructure -fmt "raw" -as "name=externalContentTablZ:string=nodZ:string=key:string=upath:uint32=upathcrc:string=rpath:string=roles";
dataStructure -fmt "raw" -as "name=mapManager_juneBackYard:string=value";
dataStructure -fmt "raw" -as "name=notes_slopesMountainsGrass_Combined:string=value";
dataStructure -fmt "raw" -as "name=mapManager_polySurface56:string=value";
dataStructure -fmt "raw" -as "name=mapManager_snapshot_Combined:string=value";
dataStructure -fmt "raw" -as "name=notes_wildPatchH_parShape:string=value";
dataStructure -fmt "raw" -as "name=notes_pPlane4:string=value";
dataStructure -fmt "raw" -as "name=notes_trees_left1:string=value";
dataStructure -fmt "raw" -as "name=notes_pPlane2:string=value";
dataStructure -fmt "raw" -as "name=notes_groundWoods_c_geo1:string=value";
dataStructure -fmt "raw" -as "name=notes_wildPatchD_parShape:string=value";
dataStructure -fmt "raw" -as "name=mapManager_pPlane2:string=value";
dataStructure -fmt "raw" -as "name=notes_suelo:string=value";
dataStructure -fmt "raw" -as "name=mapManager_trees_left:string=value";
dataStructure -fmt "raw" -as "name=notes_wildPatchC_parShape:string=value";
dataStructure -fmt "raw" -as "name=notes_pPlane6:string=value";
dataStructure -fmt "raw" -as "name=mapManager_trees_left1:string=value";
dataStructure -fmt "raw" -as "name=notes_groundA_parShape:string=value";
dataStructure -fmt "raw" -as "name=mapManager_pPlane1:string=value";
dataStructure -fmt "raw" -as "name=notes_ground:string=value";
dataStructure -fmt "raw" -as "name=notes_wildPatchG_parShape:string=value";
dataStructure -fmt "raw" -as "name=mapManager_base_right:string=value";
dataStructure -fmt "raw" -as "name=idStructure:int32=ID";
dataStructure -fmt "raw" -as "name=notes_baseLeaves:string=value";
dataStructure -fmt "raw" -as "name=notes_grass_c_geo1:string=value";
dataStructure -fmt "raw" -as "name=notes_grassJuneBackYard_parShape:string=value";
dataStructure -fmt "raw" -as "name=notes_decayGrassPatchD_parShape:string=value";
dataStructure -fmt "raw" -as "name=notes_snapshot_Combined:string=value";
dataStructure -fmt "raw" -as "name=faceConnectMarkerStructure:bool=faceConnectMarker:string[200]=faceConnectOutputGroups";
dataStructure -fmt "raw" -as "name=notes_degraded:string=value";
dataStructure -fmt "raw" -as "name=faceConnectOutputStructure:bool=faceConnectOutput:string[200]=faceConnectOutputAttributes:string[200]=faceConnectOutputGroups";
dataStructure -fmt "raw" -as "name=notes_pPlane5:string=value";
dataStructure -fmt "raw" -as "name=notes_base_left:string=value";
dataStructure -fmt "raw" -as "name=notes_polySurface56:string=value";
dataStructure -fmt "raw" -as "name=mapManager_snapshot_CombinedGrass:string=value";
dataStructure -fmt "raw" -as "name=mapManager_baseLeaves:string=value";
dataStructure -fmt "raw" -as "name=mapManager_ground_c_geo:string=value";
dataStructure -fmt "raw" -as "name=notes_snapshot_floor:string=value";
dataStructure -fmt "raw" -as "name=notes_ground_c_geo:string=value";
dataStructure -fmt "raw" -as "name=mapManager_floorOrangeConcrete_c_geo:string=value";
dataStructure -fmt "raw" -as "name=FBXFastExportSetting_MB:string=19424";
dataStructure -fmt "raw" -as "name=mapManager_grassBase:string=value";
dataStructure -fmt "raw" -as "name=notes_base_right:string=value";
dataStructure -fmt "raw" -as "name=notes_left_parShape:string=value";
dataStructure -fmt "raw" -as "name=mapManager_slopesGroundGrassA_Combined:string=value";
dataStructure -fmt "raw" -as "name=notes_floorOrangeConcrete_c_geo:string=value";
dataStructure -fmt "raw" -as "name=notes_slopesGroundGrassD_Combined:string=value";
dataStructure -fmt "raw" -as "name=notes_pPlane1:string=value";
dataStructure -fmt "raw" -as "name=mapManager_pPlane3:string=value";
dataStructure -fmt "raw" -as "name=mapManager_grass_c_geo1:string=value";
dataStructure -fmt "raw" -as "name=notes_wildPatchE_parShape:string=value";
dataStructure -fmt "raw" -as "name=mapManager_slopesMountainsGrass_Combined:string=value";
dataStructure -fmt "raw" -as "name=mapManager_baseScatt:string=value";
dataStructure -fmt "raw" -as "name=notes_slopesGroundGrassB_Combined:string=value";
dataStructure -fmt "raw" -as "name=notes_slopesGroundGrassA_Combined:string=value";
dataStructure -fmt "raw" -as "name=notes_ferns_parShape:string=value";
dataStructure -fmt "raw" -as "name=notes_juneBackYard:string=value";
dataStructure -fmt "raw" -as "name=notes_trees_left:string=value";
dataStructure -fmt "raw" -as "name=notes_decayLeavesCarousel_parShape:string=value";
dataStructure -fmt "raw" -as "name=mapManager_slopesGroundGrassC_Combined:string=value";
dataStructure -fmt "raw" -as "name=notes_decayGrassesCenter_parShape:string=value";
dataStructure -fmt "raw" -as "name=notes_baseScatt:string=value";
dataStructure -fmt "raw" -as "name=mapManager_suelo:string=value";
dataStructure -fmt "raw" -as "name=notes_wildPatchA_parShape:string=value";
dataStructure -fmt "raw" -as "name=notes_slopesGroundGrassC_Combined:string=value";
dataStructure -fmt "raw" -as "name=Blur3dMetaData:string=Blur3dValue";
dataStructure -fmt "raw" -as "name=notes_grass_c_geo:string=value";
dataStructure -fmt "raw" -as "name=mapManager_slopesGroundGrassB_Combined:string=value";
dataStructure -fmt "raw" -as "name=notes_decayLeaves_parShape:string=value";
dataStructure -fmt "raw" -as "name=FBXFastExportSetting_FBX:string=54";
dataStructure -fmt "raw" -as "name=mapManager_degraded:string=value";
dataStructure -fmt "raw" -as "name=notes_decayGrassPatchC_parShape:string=value";
dataStructure -fmt "raw" -as "name=mapManager_base_left:string=value";
dataStructure -fmt "raw" -as "name=notes_right_parShape:string=value";
dataStructure -fmt "raw" -as "name=mapManager_slopesGroundGrassD_Combined:string=value";
dataStructure -fmt "raw" -as "name=notes_slopes_parShape:string=value";
dataStructure -fmt "raw" -as "name=mapManager_pPlane4:string=value";
dataStructure -fmt "raw" -as "name=notes_grassBase:string=value";
dataStructure -fmt "raw" -as "name=notes_base_hojas:string=value";
dataStructure -fmt "raw" -as "name=notes_bushes_parShape:string=value";
dataStructure -fmt "raw" -as "name=mapManager_pPlane5:string=value";
dataStructure -fmt "raw" -as "name=mapManager_ground:string=value";
dataStructure -fmt "raw" -as "name=notes_wildPatchF_parShape:string=value";
dataStructure -fmt "raw" -as "name=notes_wildPatchDegraded_parShape:string=value";
dataStructure -fmt "raw" -as "name=notes_decayGrassPatchA_parShape:string=value";
dataStructure -fmt "raw" -as "name=notes_widlPatchB_parShape:string=value";
dataStructure -fmt "raw" -as "name=mapManager_base_hojas:string=value";
dataStructure -fmt "raw" -as "name=notes_groundD_parShape:string=value";
dataStructure -fmt "raw" -as "name=mapManager_snapshot_floor:string=value";
dataStructure -fmt "raw" -as "name=mapManager_groundWoods_c_geo1:string=value";
dataStructure -fmt "raw" -as "name=mapManager_baseScatter:string=value";
dataStructure -fmt "raw" -as "name=notes_baseScatter:string=value";
dataStructure -fmt "raw" -as "name=notes_decayGrassPatchB_parShape:string=value";
dataStructure -fmt "raw" -as "name=notes_snapshot_CombinedGrass:string=value";
dataStructure -fmt "raw" -as "name=notes_groundC_parShape:string=value";
dataStructure -fmt "raw" -as "name=notes_trees_parShape:string=value";
dataStructure -fmt "raw" -as "name=notes_groundB_parShape:string=value";
dataStructure -fmt "raw" -as "name=notes_mountains_parShape:string=value";
// End of Vis.ma
