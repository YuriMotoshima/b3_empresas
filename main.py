from scripts.selenium_driver import configChromeDriver, check_exists_elements
import pandas as pd

wb = configChromeDriver(webVisible=False)
wb.get(url="http://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/empresas-listadas.htm")

wb.find_element_by_id("onetrust-accept-btn-handler").click()

wb.switch_to.frame("bvmf_iframe")

select_emp = [n.text for n in wb.find_element_by_class_name("inline-list-letra").find_elements_by_tag_name("a")]

for n in select_emp:
    wb.find_element_by_link_text(n).click()
    check_exists_elements(wb=wb, method="css_selector", element="table[id='ctl00_contentPlaceHolderConteudo_BuscaNomeEmpresa1_grdEmpresa_ctl01']")

    table = wb.find_element_by_css_selector("table[id='ctl00_contentPlaceHolderConteudo_BuscaNomeEmpresa1_grdEmpresa_ctl01']").get_attribute("outerHTML")
    df = pd.read_html(table, header=0, index_col=False)[0]
    print(df.shape)
    wb.find_element_by_id("ctl00_botaoNavegacaoVoltar").click()

wb.quit()
print(wb)

