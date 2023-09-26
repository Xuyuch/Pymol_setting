set matrix_mode, 1
set movie_panel, 0
set scene_buttons, 1
set cache_frames, 1
viewport 1080, 1080

set ray_shadows,0
as sticks, all
set_bond stick_radius, 0.5, all
spectrum b, rainbow, all, 1, 20

extract chr1_mat, chain "chr1(mat)"
extract chr1_pat, chain "chr1(pat)"
extract chr10_mat, chain "chr10(mat)"
extract chr10_pat, chain "chr10(pat)"
extract chr11_mat, chain "chr11(mat)"
extract chr11_pat, chain "chr11(pat)"
extract chr12_mat, chain "chr12(mat)"
extract chr12_pat, chain "chr12(pat)"
extract chr13_mat, chain "chr13(mat)"
extract chr13_pat, chain "chr13(pat)"
extract chr14_mat, chain "chr14(mat)"
extract chr14_pat, chain "chr14(pat)"
extract chr15_mat, chain "chr15(mat)"
extract chr15_pat, chain "chr15(pat)"
extract chr16_mat, chain "chr16(mat)"
extract chr16_pat, chain "chr16(pat)"
extract chr17_mat, chain "chr17(mat)"
extract chr17_pat, chain "chr17(pat)"
extract chr18_mat, chain "chr18(mat)"
extract chr18_pat, chain "chr18(pat)"
extract chr19_mat, chain "chr19(mat)"
extract chr19_pat, chain "chr19(pat)"
extract chr2_mat, chain "chr2(mat)"
extract chr2_pat, chain "chr2(pat)"
extract chr3_mat, chain "chr3(mat)"
extract chr3_pat, chain "chr3(pat)"
extract chr4_mat, chain "chr4(mat)"
extract chr4_pat, chain "chr4(pat)"
extract chr5_mat, chain "chr5(mat)"
extract chr5_pat, chain "chr5(pat)"
extract chr6_mat, chain "chr6(mat)"
extract chr6_pat, chain "chr6(pat)"
extract chr7_mat, chain "chr7(mat)"
extract chr7_pat, chain "chr7(pat)"
extract chr8_mat, chain "chr8(mat)"
extract chr8_pat, chain "chr8(pat)"
extract chr9_mat, chain "chr9(mat)"
extract chr9_pat, chain "chr9(pat)"
extract chrX_mat, chain "chrX(mat)"
extract chrX_pat, chain "chrX(pat)"

delete everything chrX_mat
delete everything chrX_pat

set_view (\
     0.750269890,    0.324408263,    0.576068759,\
     0.147000015,    0.767668426,   -0.623760700,\
    -0.644581974,    0.552670181,    0.528270006,\
     0.000002384,    0.000001788, -1049.974853516,\
    -6.021775723,   -6.870912552,   -2.041615725,\
   812.712585449, 1287.237182617,  -20.000000000 )

mset 1 x240

   
frame 1
mview store, object=chr1_mat
mview store, object=chr1_pat
mview store, object=chr10_mat
mview store, object=chr10_pat
mview store, object=chr11_mat
mview store, object=chr11_pat
mview store, object=chr12_mat
mview store, object=chr12_pat
mview store, object=chr13_mat
mview store, object=chr13_pat
mview store, object=chr14_mat
mview store, object=chr14_pat
mview store, object=chr15_mat
mview store, object=chr15_pat
mview store, object=chr16_mat
mview store, object=chr16_pat
mview store, object=chr17_mat
mview store, object=chr17_pat
mview store, object=chr18_mat
mview store, object=chr18_pat
mview store, object=chr19_mat
mview store, object=chr19_pat
mview store, object=chr2_mat
mview store, object=chr2_pat
mview store, object=chr3_mat
mview store, object=chr3_pat
mview store, object=chr4_mat
mview store, object=chr4_pat
mview store, object=chr5_mat
mview store, object=chr5_pat
mview store, object=chr6_mat
mview store, object=chr6_pat
mview store, object=chr7_mat
mview store, object=chr7_pat
mview store, object=chr8_mat
mview store, object=chr8_pat
mview store, object=chr9_mat
mview store, object=chr9_pat
mview store, object=chrX_mat
mview store, object=chrX_pat
mview store

frame 61
mview store, object=chr1_mat
mview store, object=chr1_pat
mview store, object=chr10_mat
mview store, object=chr10_pat
mview store, object=chr11_mat
mview store, object=chr11_pat
mview store, object=chr12_mat
mview store, object=chr12_pat
mview store, object=chr13_mat
mview store, object=chr13_pat
mview store, object=chr14_mat
mview store, object=chr14_pat
mview store, object=chr15_mat
mview store, object=chr15_pat
mview store, object=chr16_mat
mview store, object=chr16_pat
mview store, object=chr17_mat
mview store, object=chr17_pat
mview store, object=chr18_mat
mview store, object=chr18_pat
mview store, object=chr19_mat
mview store, object=chr19_pat
mview store, object=chr2_mat
mview store, object=chr2_pat
mview store, object=chr3_mat
mview store, object=chr3_pat
mview store, object=chr4_mat
mview store, object=chr4_pat
mview store, object=chr5_mat
mview store, object=chr5_pat
mview store, object=chr6_mat
mview store, object=chr6_pat
mview store, object=chr7_mat
mview store, object=chr7_pat
mview store, object=chr8_mat
mview store, object=chr8_pat
mview store, object=chr9_mat
mview store, object=chr9_pat
mview store, object=chrX_mat
mview store, object=chrX_pat
turn y,90
mview store

frame 121
translate [-8.885234832485448,-65.19547749132258,-28.592037777515735], object=chr1_mat, camera=0
translate [-59.64662893145116,-31.46008596658822,-43.045533461920044], object=chr1_pat, camera=0
translate [42.87989526202709,-46.24092879359561,-5.182781757566316], object=chr10_mat, camera=0
translate [98.5812750284023,8.818223566822985,22.814575639091466], object=chr10_pat, camera=0
translate [-28.957032586863132,71.58363706319493,4.09618531489466], object=chr11_mat, camera=0
translate [39.326105680815324,-47.58561684544734,49.88231770553582], object=chr11_pat, camera=0
translate [36.32947227912007,11.674670572267775,-48.54924445627425], object=chr12_mat, camera=0
translate [55.98395451123402,-61.55657652375983,-56.18768986174152], object=chr12_pat, camera=0
translate [18.422126758395557,52.78822641561593,-38.0350737608067], object=chr13_mat, camera=0
translate [79.17073339209546,-36.637669325412475,7.11635794705629], object=chr13_pat, camera=0
translate [-62.805062020858315,-27.248282910864777,6.777667649252551], object=chr14_mat, camera=0
translate [-54.99770860966361,67.39290607796246,60.383834229722304], object=chr14_pat, camera=0
translate [36.82157159630823,74.99053132425468,17.500194057762624], object=chr15_mat, camera=0
translate [-31.789174071098603,83.01025324443543,47.350042276952905], object=chr15_pat, camera=0
translate [65.81180787641618,77.68154694141603,-22.479967935363234], object=chr16_mat, camera=0
translate [-35.800513297110456,-80.68090211144496,-40.99467923967974], object=chr16_pat, camera=0
translate [47.763914439573746,98.01080978896533,14.858951599932361], object=chr17_mat, camera=0
translate [10.626906519637316,104.86056103851045,-5.994202114107965], object=chr17_pat, camera=0
translate [-42.112962652150586,-104.63261646234675,15.835954788523559], object=chr18_mat, camera=0
translate [-28.687133173610246,44.22341492681917,-32.96583337620507], object=chr18_pat, camera=0
translate [-50.71579569131991,16.12915706107455,7.142277574309404], object=chr19_mat, camera=0
translate [-50.37861853576082,19.1446356073635,-63.429445942433], object=chr19_pat, camera=0
translate [-58.95711927616772,46.29537400030919,3.078273336327847], object=chr2_mat, camera=0
translate [-12.032195328673708,4.450069368506595,-29.81981616650036], object=chr2_pat, camera=0
translate [40.0582442399505,-91.69143136403325,-24.971161813617282], object=chr3_mat, camera=0
translate [89.71637447002244,35.01457139886295,1.6678841897165424], object=chr3_pat, camera=0
translate [32.17047774062824,-30.958011203671354,-63.509556390557066], object=chr4_mat, camera=0
translate [-97.5099903618937,19.650656952781617,26.054945335032656], object=chr4_pat, camera=0
translate [-5.536446465571959,-91.03850672920592,27.551209646245837], object=chr5_mat, camera=0
translate [68.46525366489332,-11.507072159459105,43.2864961923477], object=chr5_pat, camera=0
translate [-74.02194219947295,-8.552862832019827,13.928120984783146], object=chr6_mat, camera=0
translate [-58.186735415884144,-73.34936747900164,-15.60458099074317], object=chr6_pat, camera=0
translate [64.1193606190633,3.351336943549512,-13.888994595937088], object=chr7_mat, camera=0
translate [-57.57520595433772,23.16317919187788,80.98340307127899], object=chr7_pat, camera=0
translate [55.65659080342928,-75.27177016703578,40.36729800392344], object=chr8_mat, camera=0
translate [-14.24043201008946,39.80962721900073,0.7746906874016402], object=chr8_pat, camera=0
translate [-19.83738453675443,-7.793312320092241,-57.4013878052101], object=chr9_mat, camera=0
translate [-69.45704840437881,-2.9485798982246227,67.47689152028079], object=chr9_pat, camera=0
translate [51.32132444036537,43.842229985264694,-2.2171379729313756], object=chrX_mat, camera=0
translate [-7.87475386879951,113.02760836842364,38.382471637822746], object=chrX_pat, camera=0
mview store, object=chr1_mat
mview store, object=chr1_pat
mview store, object=chr10_mat
mview store, object=chr10_pat
mview store, object=chr11_mat
mview store, object=chr11_pat
mview store, object=chr12_mat
mview store, object=chr12_pat
mview store, object=chr13_mat
mview store, object=chr13_pat
mview store, object=chr14_mat
mview store, object=chr14_pat
mview store, object=chr15_mat
mview store, object=chr15_pat
mview store, object=chr16_mat
mview store, object=chr16_pat
mview store, object=chr17_mat
mview store, object=chr17_pat
mview store, object=chr18_mat
mview store, object=chr18_pat
mview store, object=chr19_mat
mview store, object=chr19_pat
mview store, object=chr2_mat
mview store, object=chr2_pat
mview store, object=chr3_mat
mview store, object=chr3_pat
mview store, object=chr4_mat
mview store, object=chr4_pat
mview store, object=chr5_mat
mview store, object=chr5_pat
mview store, object=chr6_mat
mview store, object=chr6_pat
mview store, object=chr7_mat
mview store, object=chr7_pat
mview store, object=chr8_mat
mview store, object=chr8_pat
mview store, object=chr9_mat
mview store, object=chr9_pat
mview store, object=chrX_mat
mview store, object=chrX_pat
turn y,180
mview store

frame 240
mview store, object=chr1_mat
mview store, object=chr1_pat
mview store, object=chr10_mat
mview store, object=chr10_pat
mview store, object=chr11_mat
mview store, object=chr11_pat
mview store, object=chr12_mat
mview store, object=chr12_pat
mview store, object=chr13_mat
mview store, object=chr13_pat
mview store, object=chr14_mat
mview store, object=chr14_pat
mview store, object=chr15_mat
mview store, object=chr15_pat
mview store, object=chr16_mat
mview store, object=chr16_pat
mview store, object=chr17_mat
mview store, object=chr17_pat
mview store, object=chr18_mat
mview store, object=chr18_pat
mview store, object=chr19_mat
mview store, object=chr19_pat
mview store, object=chr2_mat
mview store, object=chr2_pat
mview store, object=chr3_mat
mview store, object=chr3_pat
mview store, object=chr4_mat
mview store, object=chr4_pat
mview store, object=chr5_mat
mview store, object=chr5_pat
mview store, object=chr6_mat
mview store, object=chr6_pat
mview store, object=chr7_mat
mview store, object=chr7_pat
mview store, object=chr8_mat
mview store, object=chr8_pat
mview store, object=chr9_mat
mview store, object=chr9_pat
mview store, object=chrX_mat
mview store, object=chrX_pat

mview store
get_view

### cut below here and paste into script ###
set_view (\
     0.634197712,    0.324407518,    0.701821685,\
     0.256980896,    0.767668784,   -0.587066114,\
    -0.729214430,    0.552669883,    0.403487027,\
     0.000002384,    0.000001788, -1049.974853516,\
    -6.021775723,   -6.870912552,   -2.041615725,\
   812.712585449, 1287.237182617,  -20.000000000 )
### cut above here and paste into script ###


mview reinterpolate, power=1

#maybe get view here.

as sticks, B.exp.n
set_bond stick_radius, 0.5, B.exp.n
spectrum b, rainbow, B.exp.n, 1, 21
hide everything, b.exp.n
extract b_chr1_mat, b.exp.n and chain "chr1(mat)"
extract b_chr1_pat, b.exp.n and chain "chr1(pat)"
extract b_chr10_mat, b.exp.n and chain "chr10(mat)"
extract b_chr10_pat, b.exp.n and chain "chr10(pat)"
extract b_chr11_mat, b.exp.n and chain "chr11(mat)"
extract b_chr11_pat, b.exp.n and chain "chr11(pat)"
extract b_chr12_mat, b.exp.n and chain "chr12(mat)"
extract b_chr12_pat, b.exp.n and chain "chr12(pat)"
extract b_chr13_mat, b.exp.n and chain "chr13(mat)"
extract b_chr13_pat, b.exp.n and chain "chr13(pat)"
extract b_chr14_mat, b.exp.n and chain "chr14(mat)"
extract b_chr14_pat, b.exp.n and chain "chr14(pat)"
extract b_chr15_mat, b.exp.n and chain "chr15(mat)"
extract b_chr15_pat, b.exp.n and chain "chr15(pat)"
extract b_chr16_mat, b.exp.n and chain "chr16(mat)"
extract b_chr16_pat, b.exp.n and chain "chr16(pat)"
extract b_chr17_mat, b.exp.n and chain "chr17(mat)"
extract b_chr17_pat, b.exp.n and chain "chr17(pat)"
extract b_chr18_mat, b.exp.n and chain "chr18(mat)"
extract b_chr18_pat, b.exp.n and chain "chr18(pat)"
extract b_chr19_mat, b.exp.n and chain "chr19(mat)"
extract b_chr19_pat, b.exp.n and chain "chr19(pat)"
extract b_chr2_mat, b.exp.n and chain "chr2(mat)"
extract b_chr2_pat, b.exp.n and chain "chr2(pat)"
extract b_chr3_mat, b.exp.n and chain "chr3(mat)"
extract b_chr3_pat, b.exp.n and chain "chr3(pat)"
extract b_chr4_mat, b.exp.n and chain "chr4(mat)"
extract b_chr4_pat, b.exp.n and chain "chr4(pat)"
extract b_chr5_mat, b.exp.n and chain "chr5(mat)"
extract b_chr5_pat, b.exp.n and chain "chr5(pat)"
extract b_chr6_mat, b.exp.n and chain "chr6(mat)"
extract b_chr6_pat, b.exp.n and chain "chr6(pat)"
extract b_chr7_mat, b.exp.n and chain "chr7(mat)"
extract b_chr7_pat, b.exp.n and chain "chr7(pat)"
extract b_chr8_mat, b.exp.n and chain "chr8(mat)"
extract b_chr8_pat, b.exp.n and chain "chr8(pat)"
extract b_chr9_mat, b.exp.n and chain "chr9(mat)"
extract b_chr9_pat, b.exp.n and chain "chr9(pat)"
extract b_chrX_mat, b.exp.n and chain "chrX(mat)"
extract b_chrX_pat, b.exp.n and chain "chrX(pat)"

'''
extract c_chr1_mat, c.exp.n and chain "chr1(mat)"
extract c_chr1_pat, c.exp.n and chain "chr1(pat)"
extract c_chr10_mat, c.exp.n and chain "chr10(mat)"
extract c_chr10_pat, c.exp.n and chain "chr10(pat)"
extract c_chr11_mat, c.exp.n and chain "chr11(mat)"
extract c_chr11_pat, c.exp.n and chain "chr11(pat)"
extract c_chr12_mat, c.exp.n and chain "chr12(mat)"
extract c_chr12_pat, c.exp.n and chain "chr12(pat)"
extract c_chr13_mat, c.exp.n and chain "chr13(mat)"
extract c_chr13_pat, c.exp.n and chain "chr13(pat)"
extract c_chr14_mat, c.exp.n and chain "chr14(mat)"
extract c_chr14_pat, c.exp.n and chain "chr14(pat)"
extract c_chr15_mat, c.exp.n and chain "chr15(mat)"
extract c_chr15_pat, c.exp.n and chain "chr15(pat)"
extract c_chr16_mat, c.exp.n and chain "chr16(mat)"
extract c_chr16_pat, c.exp.n and chain "chr16(pat)"
extract c_chr17_mat, c.exp.n and chain "chr17(mat)"
extract c_chr17_pat, c.exp.n and chain "chr17(pat)"
extract c_chr18_mat, c.exp.n and chain "chr18(mat)"
extract c_chr18_pat, c.exp.n and chain "chr18(pat)"
extract c_chr19_mat, c.exp.n and chain "chr19(mat)"
extract c_chr19_pat, c.exp.n and chain "chr19(pat)"
extract c_chr2_mat, c.exp.n and chain "chr2(mat)"
extract c_chr2_pat, c.exp.n and chain "chr2(pat)"
extract c_chr3_mat, c.exp.n and chain "chr3(mat)"
extract c_chr3_pat, c.exp.n and chain "chr3(pat)"
extract c_chr4_mat, c.exp.n and chain "chr4(mat)"
extract c_chr4_pat, c.exp.n and chain "chr4(pat)"
extract c_chr5_mat, c.exp.n and chain "chr5(mat)"
extract c_chr5_pat, c.exp.n and chain "chr5(pat)"
extract c_chr6_mat, c.exp.n and chain "chr6(mat)"
extract c_chr6_pat, c.exp.n and chain "chr6(pat)"
extract c_chr7_mat, c.exp.n and chain "chr7(mat)"
extract c_chr7_pat, c.exp.n and chain "chr7(pat)"
extract c_chr8_mat, c.exp.n and chain "chr8(mat)"
extract c_chr8_pat, c.exp.n and chain "chr8(pat)"
extract c_chr9_mat, c.exp.n and chain "chr9(mat)"
extract c_chr9_pat, c.exp.n and chain "chr9(pat)"
extract c_chrX_mat, c.exp.n and chain "chrX(mat)"
extract c_chrX_pat, c.exp.n and chain "chrX(pat)"
