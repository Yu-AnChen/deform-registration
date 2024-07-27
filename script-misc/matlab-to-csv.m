ggg = load('matlab-Orion_CRC_allbacthes-20220602.mat')

for i = 21:40
  tablename = sprintf('dataC%02d', i)
  if isfield(ggg, tablename)
    writetable(ggg.(tablename), sprintf('%s.csv',tablename))
  else
    fprintf('%s does not exist\n', tablename);
  end
end