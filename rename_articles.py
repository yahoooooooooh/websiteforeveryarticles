import os

def rename_gaomi_articles():
    target_dir = os.path.join("articles", "gaomipuhuinianhua")
    
    # 重要提示：在运行脚本之前，请仔细检查并按需修改以下英文文件名！
    # 这些英文名是初步翻译的结果，您可能需要调整以达到“信达雅”的标准。
    renaming_map = {
        "高密扑灰年画在中学美术教学中的应用研究.md": "Research_on_Application_of_Gaomi_Puhui_New_Year_Paintings_in_Middle_School_Art_Education.md",
        "高密扑灰年画在平面设计中的应用探究.md": "Exploration_of_Application_of_Gaomi_Puhui_New_Year_Paintings_in_Graphic_Design.md",
        "高密扑灰年画文创产品设计研究.md": "Research_on_Cultural_and_Creative_Product_Design_of_Gaomi_Puhui_New_Year_Paintings.md",
        "高密扑灰年画的造型与色彩.md": "Modeling_and_Color_of_Gaomi_Puhui_New_Year_Paintings.md",
        "高密扑灰年画艺术研究.md": "Artistic_Research_on_Gaomi_Puhui_New_Year_Paintings.md",
        "高密独有的艺术画种扑灰年画.md": "Gaomis_Unique_Art_Form_Puhui_New_Year_Paintings.md",
        "高密扑灰年画的写意特征在动画创作中的运用研究.md": "Research_on_Xieyi_Features_of_Gaomi_Puhui_New_Year_Paintings_in_Animation_Creation.md",
        "高密民间艺术传奇国家非物质文化遗产高密民艺四宝”.md": "Legend_of_Gaomi_Folk_Art_National_ICH_Four_Treasures_of_Gaomi_Folk_Arts.md", # 注意原文件名末尾的引号
        "齐鲁民间传统技艺的发展与变迁以高密扑灰年画为例.md": "Development_and_Transition_of_Qilu_Folk_Traditional_Crafts_A_Case_Study_of_Gaomi_Puhui_New_Year_Paintings.md",
        "高密民间年画艺术与版画_曲绍平.md": "Gaomi_Folk_New_Year_Paintings_Art_and_Printmaking_by_QuShaoping.md",
        "高密扑灰年画图像符号的变迁与重构.md": "Transition_and_Reconstruction_of_Image_Symbols_in_Gaomi_Puhui_New_Year_Paintings.md",
        "高密扑灰年画的造型观.md": "Perspective_on_Modeling_in_Gaomi_Puhui_New_Year_Paintings.md",
        "高密扑灰年画（2）.md": "Gaomi_Puhui_New_Year_Paintings_Part2.md",
        "高密扑灰年画（3）.md": "Gaomi_Puhui_New_Year_Paintings_Part3.md",
        "高密扑灰年画的艺术特征探析_孙湘红.md": "Analysis_of_Artistic_Features_of_Gaomi_Puhui_New_Year_Paintings_by_SunXianghong.md",
        "高密扑灰年画的色彩观念.md": "Color_Concepts_in_Gaomi_Puhui_New_Year_Paintings.md",
        "高密扑灰年画视觉图形研究.md": "Research_on_Visual_Graphics_of_Gaomi_Puhui_New_Year_Paintings.md",
        "高密扑灰年画考析.md": "Examination_and_Analysis_of_Gaomi_Puhui_New_Year_Paintings.md",
        "高密扑灰年画的艺术特色_伍晴晴.md": "Artistic_Characteristics_of_Gaomi_Puhui_New_Year_Paintings_by_WuQingqing.md",
        "高密扑灰年画的历史发展及制作工艺.md": "Historical_Development_and_Production_Process_of_Gaomi_Puhui_New_Year_Paintings.md",
        "高密扑灰年画印制技艺与印制用纸的视觉表达研究.md": "Research_on_Printing_Techniques_and_Visual_Expression_of_Printing_Paper_for_Gaomi_Puhui_New_Year_Paintings.md",
        "高密扑灰年画的发展与艺术价值_葛汉卿.md": "Development_and_Artistic_Value_of_Gaomi_Puhui_New_Year_Paintings_by_GeHanqing.md", # Appears twice, ensure content is different or consolidate if identical
        "高密三绝引入初中美术课程的研究与应用.md": "Research_and_Application_of_Introducing_Gaomi_Three_Unique_Arts_into_Junior_High_Art_Curriculum.md",
        "高密扑灰年画发展与艺术价值_葛汉卿.md": "Development_and_Artistic_Value_of_Gaomi_Puhui_New_Year_Painting_by_GeHanqing_Extended.md", # Assuming this is a different article by the same author or a typo
        "高密“三绝”产业化发展研究_李祎.md": "Research_on_Industrial_Development_of_Gaomi_Three_Unique_Arts_by_LiYi.md",
        "高密扑灰年画形式初探.md": "Preliminary_Study_on_Forms_of_Gaomi_Puhui_New_Year_Paintings.md",
        "高密扑灰年画中的女性服饰审美分析_姜文彤.md": "Aesthetic_Analysis_of_Female_Costumes_in_Gaomi_Puhui_New_Year_Paintings_by_JiangWentong.md",
        "高密扑灰年画元素在老年人产品设计中的应用研究.md": "Research_on_Application_of_Gaomi_Puhui_New_Year_Painting_Elements_in_Product_Design_for_the_Elderly.md",
        "高密扑灰年画元素在现代童装中的设计应用.md": "Design_Application_of_Gaomi_Puhui_New_Year_Painting_Elements_in_Modern_Children_s_Clothing.md",
        "高密扑灰年画_社会文化人类学的关键词_焦宝.md": "Gaomi_Puhui_New_Year_Paintings_Keywords_in_Sociocultural_Anthropology_by_JiaoBao.md",
        "扑灰年画符号的形式与意义研究.md": "Research_on_Form_and_Meaning_of_Puhui_New_Year_Painting_Symbols.md",
        "高密扑灰年画——《财神》造型艺术研究_杨爱霞.md": "Artistic_Research_on_Caishen_Modeling_in_Gaomi_Puhui_New_Year_Paintings_by_YangAixia.md",
        "高密扑灰年画——《家堂》艺术研究_杨爱霞.md": "Artistic_Research_on_Jiatang_in_Gaomi_Puhui_New_Year_Paintings_by_YangAixia.md",
        "高密扑灰年画初探.md": "Initial_Exploration_of_Gaomi_Puhui_New_Year_Paintings.md", # Appears twice, check if distinct
        "高密年画现状调查_孙莎莎.md": "Survey_on_Current_Status_of_Gaomi_New_Year_Paintings_by_SunShasha.md",
        "高密年画的发展现状及其延续性.md": "Development_Status_and_Continuity_of_Gaomi_New_Year_Paintings.md",
        "高密扑灰年画 (1).md": "Gaomi_Puhui_New_Year_Paintings_Vol1.md",
        "高密三宝”民间美术色彩研究.md": "Research_on_Colors_in_Folk_Art_of_Gaomi_Three_Treasures.md",
        "高密市文化产业现状调查与思考.md": "Survey_and_Reflections_on_Current_Status_of_Gaomi_Cultural_Industry.md",
        "高密扑灰年画.md": "Gaomi_Puhui_New_Year_Paintings_Overview.md",
        "隐于民间的艺术生态山东高密扑灰年画审美内涵浅议.md": "Hidden_Folk_Art_Ecology_Aesthetic_Connotations_of_Shandong_Gaomi_Puhui_New_Year_Paintings.md",
        "非遗视野下山东高密扑灰年画”的传承与发展研究.md": "Research_on_Inheritance_and_Development_of_Shandong_Gaomi_Puhui_New_Year_Paintings_from_ICH_Perspective.md", #Trailing quote in original name
        "解析高密家堂”扑灰年画中蕴涵的民俗象征符号.md": "Analysis_of_Folkloric_Symbolism_in_Gaomi_Jiatang_Puhui_New_Year_Paintings.md",
        "民间写意雅俗共赏中国农业博物馆馆藏高密扑灰年画赏析.md": "Folk_Xieyi_Appreciation_Gaomi_Puhui_New_Year_Paintings_in_Agricultural_Museum_of_China_Collection.md",
        "民间年画的当代传承与发展以朱仙镇木版年画与高密扑灰年画为例.md": "Contemporary_Inheritance_of_Folk_New_Year_Paintings_Zhuxianzhen_and_Gaomi_Puhui_Compared.md",
        "潍坊传统民间艺术与地域文化的关系研究.md": "Research_on_Relationship_between_Weifang_Traditional_Folk_Art_and_Regional_Culture.md",
        "山东省高密民间艺术保护研究.md": "Research_on_Protection_of_Gaomi_Folk_Art_in_Shandong_Province.md",
        "浅析高密民间艺术.md": "Brief_Analysis_of_Gaomi_Folk_Art.md",
        "生态美学语境下高密扑灰年画的民俗叙事与审美文化探析.md": "Folk_Narrative_and_Aesthetic_Culture_of_Gaomi_Puhui_New_Year_Paintings_in_Ecological_Aesthetics_Context.md",
        "莫让民间手艺变“绝技”_陈鹏.md": "Dont_Let_Folk_Craftsmanship_Become_a_Lost_Art_by_ChenPeng.md",
        "陶瓷色彩高密扑灰年画非物质文化遗产现状探究.md": "Inquiry_into_Ceramic_Colors_Gaomi_Puhui_New_Year_Paintings_and_ICH_Status.md",
        "民间与文脉山东高密扑灰年画的写意性浅析.md": "Folk_Art_and_Cultural_Context_A_Brief_Analysis_of_Xieyi_Nature_in_Shandong_Gaomi_Puhui_New_Year_Paintings.md",
        "民间艺术四宝”之一高密扑灰年画.md": "One_of_Four_Treasures_of_Folk_Art_Gaomi_Puhui_New_Year_Paintings.md",
        "扑灰年画的文人情结.md": "The_Literati_Sentiment_in_Puhui_New_Year_Paintings.md",
        "云南甲马与山东高密扑灰年画的比较性研究.md": "Comparative_Study_of_Yunnan_JiaMa_and_Shandong_Gaomi_Puhui_New_Year_Paintings.md",
        "中国高密非遗文献扑灰年画美学研究.md": "Aesthetic_Research_on_Gaomi_Puhui_New_Year_Paintings_Based_on_Chinese_ICH_Literature.md",
        "杨家埠木版年画与高密扑灰年画色彩比较研究.md": "Comparative_Study_of_Colors_in_Yangjiabu_Woodblock_and_Gaomi_Puhui_New_Year_Paintings.md",
        "民间写意画：高密扑灰年画.md": "Folk_Xieyi_Painting_Gaomi_Puhui_New_Year_Paintings.md", # Appears twice
        "民间写意画高密扑灰年画.md": "Folk_Xieyi_Paintings_Gaomi_Puhui_New_Year_Art.md", # Slightly different from above
        "山东高密扑灰年画的传承与保护_王进展.md": "Inheritance_and_Protection_of_Shandong_Gaomi_Puhui_New_Year_Paintings_by_WangJinzhan.md",
        "扑灰年画女性形象在文化创意产品中的应用_董璐影.md": "Application_of_Female_Images_in_Puhui_New_Year_Paintings_for_Cultural_Creative_Products_by_DongLuying.md",
        "扑灰年画的意蕴美.md": "The_Implicit_Beauty_of_Puhui_New_Year_Paintings.md",
        "戏中有画画中有戏胶东地区戏出年画与小戏茂腔”.md": "Drama_in_Painting_Painting_in_Drama_Jiaodong_Theatrical_New_Year_Paintings_and_Maoqiang_Opera.md", #Trailing quote in original name
        "山东高密的扑灰年画”.md": "Shandong_Gaomis_Puhui_New_Year_Paintings.md", #Trailing quote in original name
        "扑灰年画与浮世绘比较研究.md": "Comparative_Study_of_Puhui_New_Year_Paintings_and_Ukiyoe.md",
        "山东高密扑灰年画研究综述.md": "Research_Review_on_Shandong_Gaomi_Puhui_New_Year_Paintings.md",
        "山东潍坊地区年画粉本田野调查.md": "Fieldwork_Survey_on_New_Year_Painting_Drafts_in_Weifang_Shandong.md",
        "家堂”何以成图？清代家堂图”中的时间秩序与空间构建.md": "How_Jiatang_Pictures_Are_Formed_Temporal_Order_and_Spatial_Construction_in_Qing_Dynasty_Jiatang_Paintings.md",
        "从下里巴人到阳春白雪高密扑灰年画代表性传承人吕蓁立访谈录.md": "From_Folk_to_Fine_Art_Interview_with_Lv_Zhenli_Representative_Inheritor_of_Gaomi_Puhui_New_Year_Paintings.md",
        "山东高密扑灰年画的构图.md": "Composition_of_Shandong_Gaomi_Puhui_New_Year_Paintings.md",
        "山东高密扑<y_bin_338>年画的历史发展与现代产业运作.md": "Historical_Development_and_Modern_Industrial_Operation_of_Shandong_Gaomi_Puhui_New_Year_Paintings.md", # Note: 扑灰 was 扑<y_bin_338> in listing output for this, assuming typo and it's 扑灰. Please verify original filename if error. If 扑<y_bin_338> is correct, the key should reflect that.
        "以墨设色”与以色代墨”的分野：高密扑灰年画的色彩美学研究.md": "Ink_for_Color_vs_Color_as_Ink_Differentiation_Color_Aesthetics_Research_of_Gaomi_Puhui_New_Year_Paintings.md",
        "坚定文化自信__创新扑灰年画非遗技艺_宋新玲.md": "Strengthening_Cultural_Confidence_Innovating_Puhui_New_Year_Painting_ICH_Techniques_by_SongXinling.md", #Double underscore in original
        "墙上贴着的非遗情怀_王天宇.md": "ICH_Sentiments_on_the_Wall_by_WangTianyu.md",
        "山东东方中国民艺博物馆馆藏高密扑灰年画.md": "Gaomi_Puhui_New_Year_Paintings_in_Shandong_Oriental_Chinese_Folk_Art_Museum_Collection.md",
        "关于扑灰年画艺术特征的研究.md": "Research_on_Artistic_Characteristics_of_Puhui_New_Year_Paintings.md",
        "唐宋绘画视域下山东高密扑灰年画.md": "Shandong_Gaomi_Puhui_New_Year_Paintings_from_Perspective_of_Tang_and_Song_Dynasty_Painting.md",
        "中国农业博物馆藏高密家堂”扑灰年画的初步研究.md": "Preliminary_Research_on_Gaomi_Jiatang_Puhui_New_Year_Paintings_in_Agricultural_Museum_of_China_Collection.md",
        "传统扑灰年画造型样式与二维动画形象设计_张瑞瑞.md": "Traditional_Puhui_New_Year_Painting_Styles_and_2D_Animation_Character_Design_by_ZhangRuiri.md",
        "优秀传统文化的魅力谈谈高密扑灰年画的创造性.md": "The_Charm_of_Excellent_Traditional_Culture_On_the_Creativity_of_Gaomi_Puhui_New_Year_Paintings.md",
        "传统绘画在平面设计中的应用以扑灰年画为例.md": "Application_of_Traditional_Painting_in_Graphic_Design_A_Case_Study_of_Puhui_New_Year_Paintings.md",
        "《高密扑灰年画展示馆》.md": "Exhibition_Hall_of_Gaomi_Puhui_New_Year_Paintings_Guide.md"
    }

    if not os.path.isdir(target_dir):
        print(f"错误：目录 '{target_dir}' 不存在。")
        return

    print(f"开始重命名目录 '{target_dir}' 下的文件...")
    renamed_count = 0
    skipped_count = 0
    error_count = 0
    not_found_count = 0

    # Create a set of values to check for duplicate new names before renaming
    new_names_set = set()
    for old_name, new_name in renaming_map.items():
        if new_name in new_names_set:
            print(f"警告：目标英文名 '{new_name}' (来自 '{old_name}') 在映射表中重复。请修改以确保唯一性。")
        new_names_set.add(new_name)


    for old_name_chinese, new_name_english in renaming_map.items():
        old_file_path = os.path.join(target_dir, old_name_chinese)
        new_file_path = os.path.join(target_dir, new_name_english)

        if not os.path.exists(old_file_path):
            # Try to find with potential quote issues for specific files observed
            # This is a basic heuristic, more robust matching might be needed if filenames are very inconsistent
            potential_fixes = [old_name_chinese.replace("”.md", ".md")]
            found_alternative = False
            for alt_name in potential_fixes:
                alt_file_path = os.path.join(target_dir, alt_name)
                if old_name_chinese != alt_name and os.path.exists(alt_file_path):
                    print(f"提示：源文件 '{old_file_path}' 未找到，但找到了 '{alt_file_path}'。将使用此文件进行重命名。")
                    old_file_path = alt_file_path
                    found_alternative = True
                    break
            
            if not found_alternative:
                print(f"警告：源文件 '{old_file_path}' 未找到，跳过。")
                not_found_count += 1
                continue

        if old_file_path == new_file_path:
            print(f"提示：源文件名和目标文件名相同 ('{old_name_chinese}')，跳过。")
            skipped_count +=1
            continue
            
        if os.path.exists(new_file_path):
            print(f"警告：目标文件 '{new_file_path}' 已存在。为避免覆盖，跳过重命名 '{old_name_chinese}'。")
            skipped_count += 1
            continue
            
        try:
            os.rename(old_file_path, new_file_path)
            print(f"成功：'{old_name_chinese}' -> '{new_name_english}'")
            renamed_count += 1
        except OSError as e:
            print(f"错误：重命名 '{old_name_chinese}' 为 '{new_name_english}' 失败: {e}")
            error_count += 1
            
    print("\n重命名操作完成。")
    print(f"成功重命名: {renamed_count} 个文件")
    print(f"源文件未找到: {not_found_count} 个文件")
    print(f"跳过 (目标已存在或同名): {skipped_count} 个文件")
    print(f"发生错误: {error_count} 个文件")

if __name__ == "__main__":
    rename_gaomi_articles()