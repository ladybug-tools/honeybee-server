

cd test/hackathon_dynamo/solaraccess

/mnt/c/Dropbox/Shared/dev/repos/honeybee-server/radiance/bin/oconv -f scene/opaque/hackathon_dynamo..opq.mat scene/opaque/hackathon_dynamo..opq.rad scene/glazing/hackathon_dynamo..glz.mat scene/glazing/hackathon_dynamo..glz.rad sky/hackathon_dynamo_suns.mat sky/hackathon_dynamo_suns.rad > hackathon_dynamo.oct
/mnt/c/Dropbox/Shared/dev/repos/honeybee-server/radiance/bin/rcontrib -dj 0.0 -dt 0.0 -I -aa 0.25 -as 128 -y 2500 -dp 64 -ab 0 -ad 512 -ss 0.0 -dc 1.0 -ds 0.5 -dr 0 -st 0.85 -lw 0.05 -M sky/hackathon_dynamo.sun -lr 4 -ar 16 hackathon_dynamo.oct < hackathon_dynamo.pts > result/hackathon_dynamo.dc
/mnt/c/Dropbox/Shared/dev/repos/honeybee-server/radiance/bin/rmtxop -c 47.4 119.9 11.6 -fa result/hackathon_dynamo.dc > result/hackathon_dynamo.ill