def class_balancer(df,id,lab,maj_cls,trs = 1,trs_red = 0.005,trd_rat = 5):
  trd_rat_res = 0
  while(trd_rat_res < (1/trd_rat)):
    df_lab_1 = df[lab].value_counts().reset_index(name = "count").rename(columns = {"index":lab})
    df_lab_1["pct_cnt"] = df_lab_1["count"]/df_lab_1["count"].sum()
    df_cnt = df.drop_duplicates()[[id,lab]].value_counts().reset_index(name = "count_lab")
    df_cnt["tot_lab"] = df_cnt.groupby(id)["count_lab"].transform("sum")
    df_cnt["pct_lab"] = df_cnt.count_lab/df_cnt.tot_lab
    rem_img = df_cnt.loc[(df_cnt[lab] == maj_cls) & (df_cnt["pct_lab"] >= trs),:][id].tolist()
    df_2 = df[~df[id].isin(rem_img)].reset_index(drop = True)
    print("Number of images removed at threshold","{:.{}f}".format(trs,len(str(trs_red).split(".")[1])),
          ":",len(rem_img),", data shape:",df_2.shape)
    df_lab_2 = df_2[lab].value_counts().reset_index(name = "count").rename(columns = {"index":lab})
    df_lab_2["pct_cnt"] = df_lab_2["count"]/df_lab_2["count"].sum()
    cnt_maj_1 = df_lab_1.loc[df_lab_1[lab] == maj_cls,"count"].values[0]
    cnt_maj_2 = df_lab_2.loc[df_lab_2[lab] == maj_cls,"count"].values[0]
    cnt_min_1 = df_lab_1.loc[df_lab_1[lab] != maj_cls,"count"].values
    cnt_min_2 = df_lab_2.loc[df_lab_2[lab] != maj_cls,"count"].values
    red_maj = (cnt_maj_1 - cnt_maj_2)/cnt_maj_1
    red_min = (cnt_min_1 - cnt_min_2)/cnt_min_1
    trd_rat_res = (red_min/red_maj).max()

    if(trd_rat_res >= (1/trd_rat)):
      print("Tradeoff ratio exceeded. Returning data with threshold at",
            "{:.{}f}".format((trs + trs_red),len(str(trs_red).split(".")[1])))
      return(df_res,rem_img_res)
    
    trs -= trs_red
    df_res = df_2
    rem_img_res = rem_img