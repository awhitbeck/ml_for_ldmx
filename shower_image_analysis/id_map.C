
void id_map(){

  TChain* t = new TChain("test_ana/t_image");
  t->Add("../samples/shower_image/4pt0_gev_electron_gun_image_tree.root");
  t->Draw("hit_posy:hit_posx>>id_0_10","hit_id/10 < 50");
  t->Draw("hit_posy:hit_posx>>id_10_20","hit_id/10 >= 50 && hit_id/10 < 100");
  t->Draw("hit_posy:hit_posx>>id_20_30","hit_id/10 >= 100 && hit_id/10 < 150");
  t->Draw("hit_posy:hit_posx>>id_30_40","hit_id/10 >= 150 && hit_id/10 < 200");
  t->Draw("hit_posy:hit_posx>>id_40_50","hit_id/10 >= 200 && hit_id/10 < 250");
  t->Draw("hit_posy:hit_posx>>id_50_60","hit_id/10 >= 250 && hit_id/10 < 300");
  t->Draw("hit_posy:hit_posx>>id_60_70","hit_id/10 >= 300 && hit_id/10 < 350");
  t->Draw("hit_posy:hit_posx>>id_70_80","hit_id/10 >= 350 && hit_id/10 < 400");
  t->Draw("hit_posy:hit_posx>>id_80_90","hit_id/10 >= 400 && hit_id/10 < 450");

  
  TH2F* id_0_10 = (TH2F*) gDirectory->Get("id_0_10");
  id_0_10->GetXaxis()->SetRangeUser(-300,300);
  id_0_10->GetYaxis()->SetRangeUser(-300,300);
  id_0_10->SetMarkerStyle(8);
  id_0_10->SetMarkerColor(1);
  id_0_10->SetMarkerSize(.4);

  TH2F* id_10_20 = (TH2F*) gDirectory->Get("id_10_20");
  id_10_20->SetMarkerStyle(8);
  id_10_20->SetMarkerColor(2);
  id_10_20->SetMarkerSize(.4);

  TH2F* id_20_30 = (TH2F*) gDirectory->Get("id_20_30");
  id_20_30->SetMarkerStyle(8);
  id_20_30->SetMarkerColor(3);
  id_20_30->SetMarkerSize(.4);

  TH2F* id_30_40 = (TH2F*) gDirectory->Get("id_30_40");
  id_30_40->SetMarkerStyle(8);
  id_30_40->SetMarkerColor(4);
  id_30_40->SetMarkerSize(.4);

  TH2F* id_40_50 = (TH2F*) gDirectory->Get("id_40_50");
  id_40_50->SetMarkerStyle(8);
  id_40_50->SetMarkerColor(5);
  id_40_50->SetMarkerSize(.4);

  TH2F* id_50_60 = (TH2F*) gDirectory->Get("id_50_60");
  id_50_60->SetMarkerStyle(8);
  id_50_60->SetMarkerColor(6);
  id_50_60->SetMarkerSize(.4);

  TH2F* id_60_70 = (TH2F*) gDirectory->Get("id_60_70");
  id_60_70->SetMarkerStyle(8);
  id_60_70->SetMarkerColor(1);
  id_60_70->SetMarkerSize(.4);

  TH2F* id_70_80 = (TH2F*) gDirectory->Get("id_70_80");
  id_70_80->SetMarkerStyle(8);
  id_70_80->SetMarkerColor(2);
  id_70_80->SetMarkerSize(.4);

  TH2F* id_80_90 = (TH2F*) gDirectory->Get("id_80_90");
  id_80_90->SetMarkerStyle(8);
  id_80_90->SetMarkerColor(3);
  id_80_90->SetMarkerSize(.4);

  id_0_10->Draw();
  id_10_20->Draw("same");
  id_20_30->Draw("same");
  id_30_40->Draw("same");  
  id_40_50->Draw("same");
  id_50_60->Draw("same");
  id_60_70->Draw("same");
  id_70_80->Draw("same");
  id_80_90->Draw("same");
    
}
